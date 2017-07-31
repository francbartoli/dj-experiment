# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from dj_experiment.urls import urlpatterns as dj_experiment_urls

urlpatterns = [
    url(r'^', include(dj_experiment_urls, namespace='dj_experiment')),
]
