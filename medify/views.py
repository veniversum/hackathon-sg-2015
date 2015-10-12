from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.core.serializers.python import Serializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import *
from functools import reduce
from .models import *
from . import  matching
# Create your views here.


def index(request):
    return render(request, "medify/index.html", {})


def pharmacies(request):
    return render(request, "medify/pharmacies.html", {})

def fuzzy_substring(needle, haystack):
    """Calculates the fuzzy match of needle in haystack,
    using a modified version of the Levenshtein distance
    algorithm.
    The function is modified from the levenshtein function
    in the bktree module by Adam Hupp"""
    m, n = len(needle), len(haystack)

    # base cases
    if m == 1:
        return needle not in haystack
    if not n:
        return m
    row1 = [0] * (n + 1)
    for i in range(0, m):
        row2 = [i + 1]
        for j in range(n):
            cost = (needle[i] != haystack[j])
            row2.append(
                min(row1[j + 1] + 1,  # deletion
                    row2[j] + 1,  # insertion
                    row1[j] + cost)  # substitution
            )
        row1 = row2
    return min(row1)

class FieldSerialiser(Serializer):
    def end_object(self, obj):
        self._current['id'] = obj._get_pk_val()
        self._current['model'] = obj._meta.object_name
        self.objects.append(self._current)

def resultsGetModels(results, model):
    return model.objects.in_bulk(reduce(
            lambda a, b: a | b,
            [r[1].get(model, set()) for r in results],
            set()))


TRIE = matching.loadTrie()
def omni_search2(request):
    if request.method == "GET":
        substring = request.GET["search"]

        results = matching.search(substring, 2, TRIE)
        
        # Extract model instances in bulk
        illegalMeds = resultsGetModels(results, IllegalMedication)
        approvedMeds = resultsGetModels(results, ApprovedMedication)
        approvedDevices = resultsGetModels(results, ApprovedDevice)
        
        # Order model instances according to edit distance
        resp = []
        for r in results:
            resp.extend([
                illegalMeds[id]
                for id in r[1].get(IllegalMedication, set())
            ])
            resp.extend([
                approvedMeds[id]
                for id in r[1].get(ApprovedMedication, set())
            ])
            resp.extend([
                approvedDevices[id]
                for id in r[1].get(ApprovedDevice, set())
            ])

        paginator = Paginator(resp, 100000)

        page = request.GET.get("page")
        try:
            resp_page = paginator.page(page)
        except PageNotAnInteger:
            resp_page = paginator.page(1)
        except EmptyPage:
            resp_page = paginator.page(paginator.num_pages)

        serializer = FieldSerialiser()
        return JsonResponse({
            "page": resp_page.number,
            "next_page": resp_page.next_page_number() if resp_page.has_next() else None,
            "num_pages": paginator.num_pages,
            "results": serializer.serialize(resp_page)
        }, safe=False)
    

def omni_search(request):
    if request.method == "GET":
        substring = request.GET["search"]

        illegalMeds = IllegalMedication.objects.all()
        approvedMeds = ApprovedMedication.objects.all()
        approvedDevices = ApprovedDevice.objects.all()

        results = {
            "illegal_medication": [],
            "approved_medication": [],
            "approved_devices": [],
        }

        illegalMedsMatch = IllegalMedication.objects.filter(Q(product_name__icontains=substring) | Q(manufacturer__icontains=substring))[:5].values()

        for item in illegalMedsMatch:
            results["illegal_medication"].append(item)

        approvedMedsMatch = ApprovedMedication.objects.filter(Q(product_name__icontains=substring) | Q(manufacturer__icontains=substring) | Q(active_ingredients__icontains=substring))[:5].values()

        for item in approvedMedsMatch:
            results["approved_medication"].append(item)

        approvedDeviceMatch = ApprovedDevice.objects.filter(Q(device_name__icontains=substring) | Q(product_owner_name__icontains=substring) | Q(models_name__icontains=substring))[:5].values()

        for item in approvedDeviceMatch:
            results["approved_devices"].append(item)

        deep_search = request.GET["deep_search"]

        if deep_search.lower() in ['true', '1', 't']:
            count = 0
            illegalMedValues = illegalMeds.values()
            for value_name in ["product_name", "manufacturer"]:
                for med in illegalMedValues:
                    if fuzzy_substring(substring.lower(), med[value_name].lower()) < 0.25 * len(substring):
                        if med not in results["illegal_medication"]:
                            results["illegal_medication"].append(med)
                            count += 1
                            if count > 3:
                                break
            count = 0
            approvedMedValues = approvedMeds.values()
            for value_name in ["product_name", "manufacturer", "active_ingredients"]:
                for med in approvedMedValues:
                    if fuzzy_substring(substring.lower(), med[value_name].lower()) < 0.25 * len(substring):
                        if med not in results["approved_medication"]:
                            results["approved_medication"].append(med)
                            count += 1
                            if count > 3:
                                break
            count = 0
            approvedDeviceValues = approvedDevices.values()
            for value_name in ["device_name", "product_owner_name", "models_name"]:
                for dev in approvedDeviceValues:
                    if fuzzy_substring(substring.lower(), dev[value_name].lower()) < 0.25 * len(substring):
                        if dev not in results["approved_devices"]:
                            results["approved_devices"].append(dev)
                            count += 1
                            if count > 3:
                                break

        return JsonResponse(results)

def adv_search(request):
    if request.method == "GET":
        approvedMeds = ApprovedMedication.objects.all()
        substring = request.GET["name"]
        if len(substring)>0:
            approvedMeds=approvedMeds.filter(product_name__icontains=substring)
        substring = request.GET["manufacturer"]
        if len(substring)>0:
            approvedMeds=approvedMeds.filter(manufacturer__icontains=substring)
        substring = request.GET["active_ingredient"]
        if len(substring)>0:
            approvedMeds=approvedMeds.filter(active_ingredients__icontains=substring)
        substring = request.GET["f_class"]
        if len(substring)>0:
            approvedMeds=approvedMeds.filter(f_class__icontains=substring)
        f_date= request.GET["fromdate"];
        if len(f_date)>0:
            if not f_date[1:2].isdigit():
                f_date = "0"+f_date;
            approvedMeds=approvedMeds.filter(approval_date__gte=datetime.strptime(f_date,"%d %B, %Y").date())
        t_date=request.GET["todate"];
        if len(t_date)>0:
            if not t_date[1:2].isdigit():
                t_date = "0"+t_date;
            approvedMeds=approvedMeds.filter(approval_date__lte=datetime.strptime(t_date,"%d %B, %Y").date())
        approvedMeds=approvedMeds[:10].values()
        results = {
            "illegal_medication": [],
            "approved_medication": [],
            "approved_devices": [],
        }
        for item in approvedMeds:
            results["approved_medication"].append(item)
            
        return JsonResponse(results)
        
            
