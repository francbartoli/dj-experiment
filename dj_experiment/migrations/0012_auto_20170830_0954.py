# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0011_auto_20170829_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dsfile',
            field=models.FilePathField(path='./', max_length=1024, recursive=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='data_dir',
            field=models.CharField(default='./', max_length=250),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='separator',
            field=models.CharField(default='.', max_length=1),
        ),
    ]
