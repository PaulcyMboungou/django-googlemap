from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^carpool/gmap/', include('geo.googlemap.urls')),
    (r'^carpool/admin/', include('django.contrib.admin.urls')),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)