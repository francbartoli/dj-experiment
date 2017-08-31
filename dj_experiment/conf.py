from appconf import AppConf
from django.conf import settings


class DjExperimentAppConf(AppConf):
    DATA_DIR = "./"
    SEPARATOR = "."
    OUTPUT_PREFIX = ""
    OUTPUT_SUFFIX = ".nc"
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_RESULT_BACKEND = 'rpc://'

    class Meta:
        prefix = 'dj_experiment'
        holder = 'dj_experiment.conf.settings'
