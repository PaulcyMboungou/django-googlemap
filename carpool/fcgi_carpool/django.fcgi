#!/usr/bin/python
import os, sys
sys.path.insert(0, "/home/xxxx/www")
os.environ['DJANGO_SETTINGS_MODULE'] = "carpool.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
