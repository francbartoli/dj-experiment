# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0002_auto_20170802_1206_squashed_0004_auto_20170802_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='xperiments',
        ),
        migrations.AddField(
            model_name='catalog',
            name='xperiments',
            field=models.ManyToManyField(related_name='catalogs', verbose_name=b'Catalog experiments', to='dj_experiment.Experiment'),
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
