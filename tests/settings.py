# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "cccccccccccccccccccccccccccccccccccccccccccccccccc"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    'django.contrib.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    'django_extensions',
    "dj_experiment",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()

# dj_experiment specific settings

DJ_EXPERIMENT_DATA_DIR = './'
DJ_EXPERIMENT_SEPARATOR = '.'
DJ_EXPERIMENT_OUTPUT_PREFIX = ""
DJ_EXPERIMENT_OUTPUT_SUFFIX = ".nc"
