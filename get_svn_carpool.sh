#!/bin/sh
# run from ~/www/projects
echo 'export from svn'
cd ${HOME}/projects
svn export --force http://django-googlemap.googlecode.com/svn/trunk/ carpooling
chmod +x get_svn_carpool.sh

cd carpooling/carpool
PYTHONPATH=${HOME}/projects/carpooling:$HOME python manage.py syncdb
cd ..
cp -r static $HOME

cd $HOME
ln -s projects/carpooling/carpool/fcgi_carpool carpool

chmod +x carpool/django.fcgi
