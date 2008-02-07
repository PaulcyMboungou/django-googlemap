#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from geo.googlemap.models import *
from django.contrib.sessions.models import Session

class UserDirLink(models.Model):
    user  = models.CharField(max_length=100)
    direction = models.ForeignKey(GDirection)
    distmax = models.IntegerField(default=1, help_text='kilometers')
    zonelat = models.IntegerField(default=0)
    zonelon = models.IntegerField(default=0)
    class Admin:
        list_display = ('user', 'direction', 'distmax')

class DirLink(models.Model):
    dir1 = models.ForeignKey(GDirection, related_name='link1_set')
    dir2 = models.ForeignKey(GDirection, related_name='link2_set')
    distmax = models.IntegerField(default=0, help_text='kilometers')
    class Admin:
        pass

class Plant(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    desc = models.TextField(verbose_name='description')
    code = models.CharField(max_length=50, verbose_name='code')
    position = models.ForeignKey(GLatLng)
    image = models.ImageField(upload_to='plants')
    
    def display(self):
        return '<img src=%s>' % self.get_image_url()
    display.allow_tags=True
    class Admin:
        list_display = ('name', 'image', 'display', 'position')
