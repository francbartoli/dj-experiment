from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
#from dj_experiment.apps.interactions.schedule import SCHEDULE
from django.apps import AppConfig, apps
from django.conf import settings

if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'example.settings')  # pragma: no cover


app = Celery('example.tasksapp', backend='rpc://',
             include=['dj_experiment.tasks.tasks'])


class CeleryConfig(AppConfig):
    name = 'example.tasksapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker doesn't have to serialize
        # the configuration object to child processes.
        # - namespace='CELERY' means all celery-related configuration keys
        #   should have a `CELERY_` prefix.
        app.config_from_object('django.conf:settings',
                               namespace='DJ_EXPERIMENT_CELERY')
        installed_apps = [
            app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover


# set schedule
# app.conf.CELERYBEAT_SCHEDULE = SCHEDULE
