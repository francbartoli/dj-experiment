# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0004_auto_20170803_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='name',
        ),
        migrations.AddField(
            model_name='basemodel',
            name='name',
            field=models.CharField(
                default='rkh', unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
