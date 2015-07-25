from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "medify/index.html", {})


def pharmacies(request):
    return render(request, "medify/pharmacies.html", {})
