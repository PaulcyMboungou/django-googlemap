#!/bin/sh
echo 'export from svn'
svn export --force http://django-googlemap.googlecode.com/svn/trunk/ .

chmod +x get_svn_carpool.sh
cd carpool
mv fcgi_carpool/django.fcgi .
mv fcgi_carpool/.htaccess .
chmod +x django.fcgi

python manage.py syncdb --pythonpath=..
