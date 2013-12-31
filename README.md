# Django GTD

A sample *Getting Things Done* (GTD) app using PostgreSQL, Memcached and the Django admin
interface. To create projects, actions, context or make any modifications, use
the Django admin URL at ``http://<app-url>/admin/``.

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Want to use PostgreSQL?

To use mysql instead of postgresql on production, you need to make only a few
changes before pushing (or updating) your app:

  * In stackato.yml, replace `mysql` with `postgresql` under *services*.
  * In stackato.yml, replace `mysql-python` with `psycopg2` under *requirements*.

## License

The original page (http://code.google.com/p/django-gtd/) listed "Code license
GNU GPL v3" on December 30, 2013 when I'm writing this.  Since I do not see anything 
to the contrary in any of the pages and since a search for 'copy', 'copyright', '(c)'
and 'license' only turn up the pre-rebase.sample in the .git folder, I will operate
under the assumption that all contributors intended to contribute their code under
GNU GPL v3.

Note that individual authors may be willing to re-license their contributions.  
(Unfortunately, it can be tedious to contact them all...)