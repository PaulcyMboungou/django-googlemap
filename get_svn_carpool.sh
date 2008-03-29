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
echo 'GMAP_SECRET_KEY = "ABQIAAAAiehfuX-3OQswVoGEWkc9zxTD2KCBnNxmqJQ9kY2vT-1IXhqJORSfXCdOLCCX_Ec1F8r9JcDKIIh_oA"' > settings_local.py

cd $HOME
ln -s projects/carpooling/carpool/fcgi_carpool carpool

chmod +x carpool/django.fcgi
