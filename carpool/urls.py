from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^carpool/$', 'carpool.main.views.main'),
    (r'^carpool/add_dir/$', 'carpool.main.views.add_dir'),
    (r'^carpool/gmap/', include('geo.googlemap.urls')),
    (r'^carpool/admin/', include('django.contrib.admin.urls')),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
