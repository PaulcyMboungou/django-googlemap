#!/usr/bin/python
import os, sys
sys.path.insert(0, "/home/sphenex/www/projects/carpooling")
sys.path.insert(0, "/home/sphenex/www")
os.environ['DJANGO_SETTINGS_MODULE'] = "carpool.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
