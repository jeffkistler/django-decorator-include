import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(__file__)

def absolute_path(path):
    return os.path.normpath(os.path.join(BASE_DIR, path))

SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': absolute_path('database.sqlite3'),
    }
}

INSTALLED_APPS = (
    'django.contrib.sites',
    'decorator_include',
)

ROOT_URLCONF = 'decorator_include.tests.urls'
