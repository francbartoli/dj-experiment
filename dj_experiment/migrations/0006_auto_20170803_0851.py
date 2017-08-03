# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0005_auto_20170803_1341'),
    ]

    operations = [
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
