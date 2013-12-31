echo 'Run commands with:
PYTHONPATH="`pwd`" DJANGO_SETTINGS_MODULE="django_gtd.settings_production" ./venv/bin/django-admin.py  $COMMAND_NAME'
#
# I defined that as a helper shell script (substitute $1 for $COMMAND_NAME) to spare myself typing it over and over 


# This copies the example to the intended filename (if it does not exist), creates the dummy database, and makes it readable
if [[ ! -e "django_gtd/settings_production.py" ]]; then
    echo "Copying settings file..."
    cp django_gtd/example_settings_production.py django_gtd/settings_production.py
fi
touch /tmp/db_prod.sqlite
chmod a+w  /tmp/db_prod.sqlite # Your system wipes this directory - don't keep serving from tmp!!!!

# This sets up the database and runs the server
PYTHONPATH="`pwd`" DJANGO_SETTINGS_MODULE='django_gtd.settings_production' ./venv/bin/django-admin.py syncdb
PYTHONPATH="`pwd`" DJANGO_SETTINGS_MODULE='django_gtd.settings_production' ./venv/bin/django-admin.py migrate
PYTHONPATH="`pwd`" DJANGO_SETTINGS_MODULE='django_gtd.settings_production' ./venv/bin/django-admin.py runserver

# Confirmed that django_gtd.settings_production acted on /tmp/db_prod.sqlite

