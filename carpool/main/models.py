#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from geo.googlemap.models import *
from django.contrib.sessions.models import Session

class UserDirLink(models.Model):
    session_user  = models.ForeignKey(Session)
    direction = models.ForeignKey(GDirection)
    distmax = models.IntegerField(default=1, help_text='kilometers')
    zonelat = models.IntegerField(default=0)
    zonelon = models.IntegerField(default=0)
    class Admin:
        list_display = ('session_user', 'direction', 'distmax')

class DirLink(models.Model):
    dir1 = models.ForeignKey(GDirection, related_name='link1_set')
    dir2 = models.ForeignKey(GDirection, related_name='link2_set')
    distmax = models.IntegerField(default=0, help_text='kilometers')
    class Admin:
        pass

