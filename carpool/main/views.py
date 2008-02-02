#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.newforms import form_for_model, form_for_instance
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import UserDirLink, User

from geo.googlemap.models import GDirection, GMarker, GLatLng, GPoly, PolyPoint, Overlay

def main(request, template='carpool_main.html'):
    if request.method == 'POST':
        pass
    else:
        pass    
    context = {
               'gmap_width':600,
               'gmap_height':400,
               'gmap_overlays_include': 'load_dirs.js',
               'gmap_global_include': 'global.js',
               'neighbour_dirs':None}
    return render_to_response(template, context)

def add_dir(request, start, end):
    lat, lon = start.split(',')
    p1 = GLatLng.objects.create(lat=float(lat), lon=float(lon))
    lat, lon = end.split(',')
    p2 = GLatLng.objects.create(lat=float(lat), lon=float(lon))
    overlay=Overlay.objects.create(name='direction', desc='')
    poly = GPoly.objects.create(overlay=overlay, type='d')
    dir = GDirection.objects.create(start=p1, end=p2, polyline=poly)
    PolyPoint.objects.create(position=p1, poly=poly, indice=0)
    PolyPoint.objects.create(position=p2, poly=poly, indice=1)
    return HttpResponse("{'dir':%d, 'start':%d, 'end':%d}" % (dir.id, p1.id, p2.id))
