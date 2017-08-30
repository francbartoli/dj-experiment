# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0010_auto_20170829_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dsfile',
            field=models.FilePathField(path=b'RCM data', max_length=1024, recursive=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='data_dir',
            field=models.CharField(default=b'RCM data', max_length=250),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='separator',
            field=models.CharField(default=b'_', max_length=1),
        ),
    ]
