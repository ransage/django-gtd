# Note - not in use

I recommend you use somebody else's branch if you're thinking of using Django 
GTD, since I'm not actively using/working this.

I spent a day or two thinking about adopting Django-GTD to replace Tracks as 
part of a general effort to migrate to Django.  I had made some changes to Tracks
(a Ruby on Rails) app quite some time ago and lost those changes when forced to 
upgrade the application (long story).  

Anyway, I have a number of projects underway and I have convinced myself of the 
feasibility of importing my Tracks to do items into Django-GTD (with some model 
updates and scripting), so I'm going to defer the transition.  Instead, I'm 
taking a few minutes to automate xml backups and I will make the transition 
either when convenient or when our Tracks server next implodes.

...


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


