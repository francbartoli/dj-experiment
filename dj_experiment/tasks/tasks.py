from __future__ import absolute_import

import logging
import time

from celery import shared_task
from celery.contrib import rdb
from dj_experiment.models import Experiment as ModExperiment
from dj_experiment.tasks.utils.extract_files import (get_experiment, get_files,
                                                     get_keywords)


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
    # rdb.set_trace()
    print xpinst
    xpfiles = get_files(xpinst, xpinst.data_dir)
    if len(xpfiles) == 0:
        logging.info(
            "No results, the number of files retrieved is %s" % len(xpfiles))
    else:
        for xpfile in xpfiles:
            logging.debug("files are the following ===> \n %s" % xpfile[0])
            logging.debug("xpfile type is %s" % type(xpfile))
            keywords = get_keywords(xpinst, xpfile)
            logging.debug("Keywords are the following ===> %s" % keywords)
    print 'netcdf save task finished'
    # return query count from db
