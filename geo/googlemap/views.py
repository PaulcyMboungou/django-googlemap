#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseServerError
from models import GMarker, GLatLng, Overlay
from django.shortcuts import render_to_response

from models import GMap2

def add_point(request):
    if request.method == 'GET':
        try:
            lat = request.GET['lat']
            lon = request.GET['lon']
            pos = GLatLng.objects.create(lat=float(lat), lon=float(lon))
            o = Overlay.objects.create(name=request.META['REMOTE_ADDR'], desc='adresse IP')
            GMarker.objects.create(overlay=o, position=pos)
        except Exception, v:
            return HttpResponse(v)
    return HttpResponse('ok'+lat+' '+lon)

def display_map(request, mapid, template, width=400, height=300):
    
    map = GMap2.objects.get(id=mapid)
    
    context = {'gmap_map_init_js':map.init_js(),
               'gmap_width':width, 'gmap_height':height}
    return render_to_response(template, context)
