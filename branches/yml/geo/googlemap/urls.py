from django.conf.urls.defaults import *
from django.conf import settings
from views import display_map


urlpatterns = patterns('',
    (r'^test/$','django.views.generic.simple.direct_to_template', {'template':'test.html'}),
    (r'^test/circle/$','django.views.generic.simple.direct_to_template', {'template':'test_circle.html'}),
    (r'^test/input/$','django.views.generic.simple.direct_to_template', {'template':'input_points.html'}),
    (r'^test/input/addpoint/$','geo.googlemap.views.add_point'),

    (r'^display/(?P<mapid>.*)/$',display_map ,{'template':'gmap_main.html'}),
    (r'^display/(?P<mapid>.*)/addpoint/$','django.views.generic.simple.direct_to_template', {'template':'map_addpoint.html'}),
)