import os, sys, site

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
site.addsitedir(os.path.join(BASE_DIR,'venv/lib/python2.6/site-packages/'))

PROJ_NAME = os.path.basename(BASE_DIR)  # Relies on name matching, but nothing hardcoded

sys.path.insert(0, os.path.join(BASE_DIR,'venv/lib/python2.6/site-packages/') )
sys.path.insert(0, os.path.join(BASE_DIR) )
sys.path.insert(0, os.path.join(BASE_DIR, PROJ_NAME) )

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings_production" % PROJ_NAME

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

