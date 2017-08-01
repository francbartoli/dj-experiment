from django.conf import settings
from appconf import AppConf

class MyAppConf(AppConf):
    DATA_DIR = "./"
    SEPARATOR = "."

    class Meta:
            prefix = 'dj_experiment'
            holder = 'dj_experiment.conf.settings'
