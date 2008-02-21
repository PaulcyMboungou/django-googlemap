#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from models import *
from geo.googlemap.models import *

def calc_neighbours(dir, dist_max):
    others = GDirection.objects.exclude(id=dir.id)
    km2deg = 180.0 / (3.1416 * 6400.0)
    dist_deg = distmax * km2deg
    lat1, lon1, lat2, lon2 = dir.start.lat, dir.start.lon, dir.end.lat, dir.end.lon, 
    nb = 0
    for alt in others:
        if DirLink.objects.filter(dir1=dir, dir2=alt).count() > 0:
            continue
        if DirLink.objects.filter(dir2=dir, dir1=alt).count() > 0:
            continue
        if alt.start.lat > lat1 + dist_deg: continue
        if alt.start.lat < lat1 - dist_deg: continue
        if alt.start.lon > lon1 + dist_deg: continue
        if alt.start.lon < lon1 - dist_deg: continue
        if alt.end.lat > lat2 + dist_deg: continue
        if alt.end.lat < lat2 - dist_deg: continue
        if alt.end.lon > lon2 + dist_deg: continue
        if alt.end.lon < lon2 - dist_deg: continue
        
        distance = dist_deg
        d = alt.start.distdeg(lat1, lon1)
        if d < distance: distance = d
        d = alt.end.distdeg(lat2, lon2)
        if d < distance: distance = d
        distance /= km2deg
        
        Dirlink.objects.create(dir1=dir, dir2=alt, distmax=distance)
        nb += 1
        return nb

def get_marker_options(name):
    return GMarkerOptions.objects.get(title=name)

def create_marker(type, position):
    overlay=Overlay.objects.create()
    marker = GMarker.objects.create(overlay=overlay, position=position, options=get_marker_options(type))
    return marker