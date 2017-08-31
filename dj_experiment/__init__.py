from __future__ import absolute_import, unicode_literals

from dj_experiment.tasks.celery import app as celery_app

__all__ = ['celery_app']
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

__version__ = '0.1.0'
