#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class GLatLng(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='latitude')
    lon = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='longitude')
    def __unicode__(self):
        return '%f , %f' % (self.lat, self.lon)
    class Meta:
        verbose_name = 'GLatLng'
        verbose_name_plural = 'GLatLng entities'
    class Admin:
        list_display = ('id', 'lat', 'lon')

class GMap2(models.Model):
    name = models.CharField(maxlength=100, verbose_name='name')
    center = models.ForeignKey(GLatLng, null=True, blank=True)
    zoom = models.IntegerField(default=13)
    dragging_enabled = models.BooleanField(default=True)
    infowindow_enabled = models.BooleanField(default=True)
    double_clickzoom_enabled = models.BooleanField(default=True)
    continuouszoom_enabled = models.BooleanField(default=False)
    googlebar_enabled = models.BooleanField(default=False)
    scrollwheelzoom_enabled = models.BooleanField(default=False)
    
    def init_js(self):
        code = ''
        if self.center:
            code = 'map.setCenter(new GLatLng(%f, %f), %d);' % (self.center.lat, self.center.lon, self.zoom)
        if not self.dragging_enabled:
            code +='\nmap.disableDragging();'
        if not self.infowindow_enabled:
            code +='\nmap.disableInfoWindow();'
        if not self.double_clickzoom_enabled:
            code +='\nmap.disableDoubleClickZoom();'
        if self.continuouszoom_enabled:
            code +='\nmap.enableContinuousZoom();'
        if self.googlebar_enabled:
            code +='\nmap.enableGoogleBar();'
        if self.scrollwheelzoom_enabled:
            code +='\nmap.enableScrollWheelZoom();'
            
        return code
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'GMap2'
        verbose_name_plural = 'GMap2 entities'
    class Admin:
        list_display = ('name', 'center', 'zoom', 'dragging_enabled')

class Layer(models.Model):
    map = models.ForeignKey(GMap2)
    name = models.CharField(maxlength=100, verbose_name='name', null=True, blank=True)
    zorder = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    class Admin:
        list_display = ('name', 'map')

class Overlay(models.Model):
    name = models.CharField(maxlength=100, verbose_name='name')
    desc = models.CharField(maxlength=100, verbose_name='description')
    zorder = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Projection(models.Model):
    overlay = models.ForeignKey(Overlay)
    layer = models.ForeignKey(Layer)
    class Admin:
        list_display = ('overlay', 'layer')


class GPoly(models.Model):
    POLY_TYPES = (
                  ('p','polygon'),
                  ('l','polyline'),
                  ('t','path'),
                  ('c','circle'),
                  ('r','r'),
                  )
    overlay = models.OneToOneField(Overlay)
    type = models.CharField(maxlength=1, choices=POLY_TYPES)
    def __unicode__(self):
        return self.overlay.name
    class Meta:
        verbose_name = 'GPoly'
        verbose_name_plural = 'GPoly entities'
    class Admin:
        list_display = ('overlay', 'type',)

class GIcon(models.Model):
    image = models.ImageField(upload_to='icons')
    shadow = models.ImageField(upload_to='icons', null=True, blank=True)

    def display(self):
        return '<img src=%s>' % self.get_image_url()
    display.allow_tags=True
    
    def __unicode__(self):
        return self.image
    class Meta:
        verbose_name = 'GIcon'
        verbose_name_plural = 'GIcon entities'
    class Admin:
        list_display = ('image', 'shadow', 'display')

class GMarkerOptions(models.Model):
    title = models.CharField(maxlength=100, verbose_name='title')
    icon = models.ForeignKey(GIcon, null=True, blank=True)
    clickable = models.BooleanField(default=False)
    draggable = models.BooleanField(default=False)
    bouncy = models.BooleanField(default=False)
    bounce_gravity = models.IntegerField(default=1)
    
    def image(self):
        if not self.icon: return 'no icon'
        return '<img src=%s>' % self.icon.get_image_url()
    image.allow_tags=True
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'GMarkerOptions'
        verbose_name_plural = 'GMarkerOptions entities'
    class Admin:
        list_display = ('title', 'image', 'clickable', 'draggable')

class GMarker(models.Model):
    overlay = models.OneToOneField(Overlay)
    position = models.ForeignKey(GLatLng)
    options = models.ForeignKey(GMarkerOptions, null=True, blank=True)
    
    def image(self):
        if not self.options: return 'no icon'
        if not self.options.icon: return 'no icon'
        return '<img src=%s>' % self.options.icon.get_image_url()
    image.allow_tags=True
    
    def __unicode__(self):
        return self.overlay.name
    class Meta:
        verbose_name = 'GMarker'
        verbose_name_plural = 'GMarker entities'
    class Admin:
        list_display = ('overlay', 'options', 'image')

class PolyPoint(models.Model):
    position = models.ForeignKey(GLatLng, core=True)
    poly = models.ForeignKey(GPoly, edit_inline=True, num_in_admin=3, min_num_in_admin=1, num_extra_on_change=1)
    indice = models.IntegerField()
    class Meta:
        verbose_name = 'PolyPoint'
        verbose_name_plural = 'PolyPoint entities'
    class _Admin:
        list_display = ('poly', 'indice')

class GDirection(models.Model):
    query = models.CharField(maxlength=100, verbose_name='query', null=True, blank=True)
    start = models.ForeignKey(GLatLng, related_name='start_dirs', null=True, blank=True)
    end = models.ForeignKey(GLatLng, related_name='end_dirs', null=True, blank=True)
    class Meta:
        verbose_name = 'GDirection'
        verbose_name_plural = 'GDirection entities'
    class Admin:
        list_display = ('id', 'query',)

class DirectionStep(models.Model):
    point = models.ForeignKey(GLatLng, core=True)
    direction = models.ForeignKey(GDirection, edit_inline=True, num_in_admin=1, min_num_in_admin=1, num_extra_on_change=1)
    indice = models.IntegerField()
    
