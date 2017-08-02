from appconf import AppConf
from django.conf import settings


class MyAppConf(AppConf):
    DATA_DIR = "./"
    SEPARATOR = "."
    OUTPUT_PREFIX = ""
    OUTPUT_SUFFIX = ".nc"

    class Meta:
        prefix = 'dj_experiment'
        holder = 'dj_experiment.conf.settings'
