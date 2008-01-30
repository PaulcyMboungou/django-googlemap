#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.newforms import form_for_model, form_for_instance
from django.shortcuts import render_to_response
from models import UserDirLink, User

def main(request, template='carpool_main.html'):
    if request.method == 'POST':
        pass
    else:
        pass    
    context = {
               'gmap_width':600,
               'gmap_height':400,
               'gmap_overlays_include': 'load_dirs.js',
               'neighbour_dirs':None}
    return render_to_response(template, context)
