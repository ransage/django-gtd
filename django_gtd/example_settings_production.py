
from django_gtd.settings import *  # Import settings and then begin overwriting it

# The following is probably not adequate, but will at least get you up and running.
# You need to rename this file to settings_production.py


# Do not run with DEBUG set to True in production
DEBUG = TEMPLATE_DEBUG = False

# Update this appropriately
ALLOWED_HOSTS = ['127.0.0.1',
                 '.example.com', # all subdomains of example.com
                 ]

# You probably want more significant changes to your DATABASES, 
# but this lets you test the deployment only if you make the
# following file readable by the process that runs your webserver!
DATABASES['default']['NAME'] = '/tmp/db_prod.sqlite'

