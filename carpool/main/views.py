#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.newforms import form_for_model, form_for_instance
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import UserDirLink, Plant
from utils import *

from geo.googlemap.models import GDirection, GMarker, GLatLng, GPoly, PolyPoint, Overlay

def main(request, template='carpool_main.html', dir_from='Talence', dir_to='Bordeaux'):
    context = {'dir_from':dir_from,
               'dir_to':dir_to,
               'gmap_width':800,
               'gmap_height':400,
               'gmap_overlays_include': 'load_dirs.js',
               'gmap_global_include': 'global.js',
               'db_dirs': GDirection.objects.all(),
               'neighbour_dirs':None}

    if not request.session.get('user_id', default=False):
        context['user_new']=True
        request.session['user_id'] = request.META['REMOTE_ADDR']
        request.session['dir_step'] = 'init'
        context['user_state'] = 'init'
    else:
        context['user_state'] = 'alt'
    context['user_id'] = request.session['user_id']
    
    if request.session['dir_step'] == 'init':
        pass
    if request.session['dir_step'] == 'home_set':
        pass
    if request.session['dir_step'] == 'work_set':
        pass
    
    return render_to_response(template, context)

def add_dir(request, username, start, end):
    if UserDirLink.objects.filter(user=username).count() == 1:
        return HttpResponse("Already exists")
    lat, lon = start.split(',')
    p1 = GLatLng.objects.create(lat=float(lat), lon=float(lon))
    lat, lon = end.split(',')
    p2 = GLatLng.objects.create(lat=float(lat), lon=float(lon))
    overlay=Overlay.objects.create()
    poly = GPoly.objects.create(overlay=overlay, type='d')
    dir = GDirection.objects.create(start=p1, end=p2, polyline=poly)
    PolyPoint.objects.create(position=p1, poly=poly, indice=0)
    PolyPoint.objects.create(position=p2, poly=poly, indice=1)
    
    UserDirLink.objects.create(user=username, direction=dir)
    
    create_marker('home', p1)
    create_marker('work', p2)
    return HttpResponse("Saved")


def plant_add(request, id=None, code=None, template='plant_form.html', gmap_overlays_include='plant_form.js'):
    context = {'gmap_width':300,
               'gmap_height':300,
               'gmap_overlays_include':gmap_overlays_include}
    fields=['name', 'desc']
    if id and code:
        context['display_insert'] = True
        context['code'] = code
        context['id'] = id
        plant = Plant.objects.get(id=int(id), code=code)
        form = form_for_instance(plant, fields=fields)
        form = form()
    else:
        if request.method == 'POST':
            form = form_for_model(Plant, fields=fields)
            data = request.POST.copy()
            pos = GLatLng.objects.create(lat=float(data['lat']), lon=float(data['lon']))
            code = gen_string()
            data['code'] = code
            form = form(data, request.FILES)
            if form.is_valid():
                inst = form.save()
                inst.position = pos
                inst.code = code
                inst.save()
                return HttpResponseRedirect('../%d/%s/' % (inst.id, inst.code))
        else:
            form = form_for_model(Plant, fields=fields)
            form = form()
    context['form'] = form
    return render_to_response(template, context)

def home_add(request, id, code, template='plant.html'):
    plant = Plant.objects.get(id=int(id), code=code)
    context = {'gmap_width':800,
               'gmap_height':400,
               'plant': plant,
               'gmap_overlays_include': 'do_plant_dirs.js'}
    return render_to_response(template, context)

from whrandom import choice
import string
def gen_string(length=32, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])