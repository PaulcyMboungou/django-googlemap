#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from geo.googlemap.models import *

class User(models.Model):
    email = models.EmailField(null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    checked = models.BooleanField(default=False)
    ip = models.IPAddressField()
    comment = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    
    class Admin:
        list_display = ('email', 'ip', 'comment')

class UserDirLink(models.Model):
    user  = models.ForeignKey(User)
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

    
class Properties(models.Model):
    overlay = models.ForeignKey(Overlay)
    opacity = models.SmallIntegerField(default=100, help_text='0:transparent 100:opaque')
    color = models.CharField(max_length=7, null=True, blank=True, help_text='#RRGGBB')
    user = models.ForeignKey(User, null=True, blank=True)
    class Meta:
        verbose_name = 'Properties entity'
        verbose_name_plural = 'Properties entities'
    class Admin:
        list_display = ('overlay', 'color', 'opacity', 'user')
