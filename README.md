# Django GTD

A sample *Getting Things Done* (GTD) app Memcached and the Django admin
interface. To create projects, actions, context or make any modifications, use
the Django admin URL at ``http://<app-url>/admin/``.

## Local development

For development, I recommend using a virtual environment to ensure that things work cleanly
and do not collide in unexpected ways.  In this case, you can do the following

    virtualenv venv   # Use your preferred folder name, venv is in .gitignore
    ./venv/bin/pip install -r requirements.txt
    ./venv/bin/python manage.py syncdb
    ./venv/bin/python manage.py migrate
    ./venv/bin/python manage.py runserver

It uglifies these commands, but eliminates lots of sources of frustration. :-)

### Compatibility

This has been used on (at least) the following Python versions:
  - Python 2.6.6

with Django 1.6 (the version is in the requirements.txt).

## Databases

I'm still developing in sqlite3, but Stackato version was set up for postgresql...

To use mysql instead of postgresql on production, you need to make only a few
changes before pushing (or updating) your app:

  * In stackato.yml, replace `mysql` with `postgresql` under *services*.
  * In stackato.yml, replace `mysql-python` with `psycopg2` under *requirements*.

## License

The original page (http://code.google.com/p/django-gtd/) listed "Code license
GNU GPL v3" on December 30, 2013 when I'm writing this.  Since I do not see anything 
to the contrary in any of the pages and since a search for 'copy', 'copyright', '(c)'
and 'license' only turns up the pre-rebase.sample in the .git folder, I will operate
under the assumption that all contributors intended to contribute their code under
GNU GPL v3.

Note that individual authors may be willing to re-license their contributions.  
(Unfortunately, it can be tedious to contact them all...)


