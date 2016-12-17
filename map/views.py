from django.http import HttpResponse
from django.shortcuts import render
from map.services import OverpassService


def index(request):
    return HttpResponse("Hello, world. This is a religion map.")


def temples(request, lat, lon, span):
    overpass_service = OverpassService()
    context = {
        "lat": lat,
        "lon": lon,
        "span": span,
        "temples": overpass_service.get_temples_tiled(float(lat), float(lon), int(span))
    }
    return render(request, 'map/index.html', context)