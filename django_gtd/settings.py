# Django settings for djangogtd project.
import os
import sys
import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oo%8002!suh#l66c+lq+58!huhb5#wi24x!)*%5z$v)gtnzw1^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'brillixy',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'django_databrowse',
    #'django.contrib.humanize',
    'gtd',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_gtd.urls'

WSGI_APPLICATION = 'django_gtd.wsgi.application'


DATABASES = {}
if 'DATABASE_URL' in os.environ:
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASES['default'] = {
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        }
#    CACHES = {
#        'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': os.getenv('MEMCACHE_URL'),
#        }
#    }
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    elif url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en_us'

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'UTC'

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

