from __future__ import absolute_import

import logging
import os
import time

from celery import shared_task
from celery.contrib import rdb
from dj_experiment.models import Case as ModCase
from dj_experiment.models import Experiment as ModExperiment
from dj_experiment.models import FieldGroup as ModFieldGroup
from dj_experiment.models import Value as ModValue
from dj_experiment.models import (CaseBelongingness, CaseKeyValue, Dataset,
                                  FieldBelongingness, FieldKeyValue)
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
            logging.debug("file is the following ===> \n %s" % xpfile[0])
            logging.debug("xpfile type is %s" % type(xpfile))
            logging.info("############################################# \
PROCESSING NEW FILE \
# ")
            logging.info("Processing file =====> %s" % xpfile[0])
            xpoutfile, keywords, fieldcases = get_keywords(xpinst, xpfile)
            logging.info(
                "Retrieve keywords which are the following ===> %s" % keywords
            )

            if (fieldcases[0] and fieldcases[1]):
                # retrieve all couples key/value ids for FieldKeyValue
                # {u'temp': u'tas'}
                kvfield = tuple()
                kvfglist = list()
                fielddict = fieldcases[0]
                for key, value in fielddict.iteritems():
                    ofg = ModFieldGroup.objects.get(shortname=key)
                    kvfield += ((ofg.id, ofg.fieldnames.get(val=value).id),)
                # save record into FieldKeyValue for each couple
                for k, v in kvfield:
                    okvfg = FieldKeyValue.objects.create(
                        fieldname=ModFieldGroup.objects.get(pk=k),
                        value=ModValue.objects.get(pk=v)
                    )
                    kvfglist.append(okvfg.id)
                # retrieve all couples key/value ids for CaseKeyValue
                # {u'fixedperiod': u'19510101-21001231', etc.. }
                kvcases = tuple()
                kvclist = list()
                casesdict = fieldcases[1]
                for key, value in casesdict.iteritems():
                    oc = ModCase.objects.get(shortname=key)
                    kvcases += ((oc.id, oc.casevals.get(val=value).id),)
                # save record into CaseKeyValue for each couple
                for k, v in kvcases:
                    okvfg = CaseKeyValue.objects.create(
                        case=ModCase.objects.get(pk=k),
                        value=ModValue.objects.get(pk=v)
                    )
                    kvclist.append(okvfg.id)
                dsobj = Dataset.objects.create(title=xpoutfile[0],
                                               name=xpoutfile[0],
                                               dsfilename=xpoutfile[0],
                                               dsfile=os.path.join(
                    xpinst.data_dir,
                    xpoutfile[3],
                    xpoutfile[0]
                ))
                # save record into FieldBelongingness for each id in the list
                for obj in kvfglist:
                    ofb = FieldBelongingness(
                        dataset=dsobj,
                        keyvalue=FieldKeyValue.objects.get(pk=obj)
                    )
                    ofb.save()

                # save record into CaseBelongingness for each id in the list
                for obj in kvclist:
                    ocb = CaseBelongingness(
                        dataset=dsobj,
                        keyvalue=CaseKeyValue.objects.get(pk=obj)
                    )
                    ocb.save()

            else:
                logging.info("Skipping file to database insertion")

    print 'netcdf save task finished'
    # return query count from db
