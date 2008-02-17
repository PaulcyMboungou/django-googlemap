from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^carpool/$', 'carpool.main.views.main', {'dir_from':'Talence', 'dir_to':'Bordeaux'}),
    (r'^carpool/add_dir/(?P<username>.*)/(?P<start>.*)/(?P<end>.*)/$', 'carpool.main.views.add_dir'),
    (r'^carpool/plant/add/$', 'carpool.main.views.plant_add'),
    (r'^carpool/plant/(?P<id>.*)/(?P<code>.*)/add/$', 'carpool.main.views.home_add'),
    (r'^carpool/plant/(?P<id>.*)/(?P<code>.*)/$', 'carpool.main.views.plant_add'),
    (r'^carpool/gmap/', include('geo.googlemap.urls')),
    (r'^carpool/admin/', include('django.contrib.admin.urls')),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
