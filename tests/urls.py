# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from dj_experiment.urls import urlpatterns as dj_experiment_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(dj_experiment_urls, namespace='dj_experiment')),
]
