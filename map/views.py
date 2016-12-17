from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. This is a religion map.")


def temples(request, lat, lon, span):
    context = {
        "lat": lat,
        "lon": lon,
        "span": span
    }
    return render(request, 'map/index.html', context)