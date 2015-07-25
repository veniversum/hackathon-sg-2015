from django.shortcuts import render
from django.http import JsonResponse
from . import models

import subdist
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
    row1 = [0] * (n+1)
    for i in range(0, m):
        row2 = [i+1]
        for j in range(n):
            cost = (needle[i] != haystack[j])
            row2.append(
                min(row1[j+1]+1,  # deletion
                row2[j]+1,  # insertion
                row1[j]+cost)  # substitution
            )
        row1 = row2
    return min(row1)


def omni_search(request):
    if request.method == "GET":
        substring = request.GET["search"]

        illegalMeds = models.IllegalMedication.objects.all()
        approvedMeds = models.ApprovedMedication.objects.all()
        approvedDevices = models.ApprovedDevice.objects.all()

        results = {
            "illegal_medication": [],
            "approved_medication": [],
            "approved_devices": [],
        }

        illegalMedValues = illegalMeds.values()
        for value_name in ["product_name", "manufacturer"]:
            for med in illegalMedValues:
                if fuzzy_substring(substring.lower(), med[value_name].lower()) < 0.25 * len(substring):
                    if med not in results["illegal_medication"]:
                        results["illegal_medication"].append(med)

        approvedMedValues = approvedMeds.values()
        for value_name in ["product_name", "manufacturer", "active_ingredients"]:
            for med in approvedMedValues:
                if fuzzy_substring(substring.lower(), med[value_name].lower()) < 0.25 * len(substring):
                    if med not in results["approved_medication"]:
                        results["approved_medication"].append(med)

        approvedDeviceValues = approvedDevices.values()
        for value_name in ["device_name", "product_owner_name", "models_name"]:
            for dev in approvedDeviceValues:
                if fuzzy_substring(substring.lower(), dev[value_name].lower()) < 0.25 * len(substring):
                    if dev not in results["approved_devices"]:
                        results["approved_devices"].append(dev)

        return JsonResponse(results)
