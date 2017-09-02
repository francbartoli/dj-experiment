from __future__ import absolute_import

import time

from celery import shared_task
from celery.contrib import rdb
from dj_experiment.models import Experiment as ModExperiment
from dj_experiment.tasks.utils.extract_files import get_experiment


@shared_task
def longtime_add(x, y):
    print 'long time task begins'
    # sleep 5 seconds
    time.sleep(5)
    print 'long time task finished'
    return x + y


@shared_task
def netcdf_save(exp_id, dir):
    print 'netcdf save task begins'
    # do something
    xperiment = ModExperiment.objects.get(pk=exp_id)
    xpname = xperiment.name
    print 'xpname=%s' % xpname
    xpinst = get_experiment(xpname, dir)
    rdb.set_trace()
    print xpinst
    print 'netcdf save task finished'
    # return query count from db
