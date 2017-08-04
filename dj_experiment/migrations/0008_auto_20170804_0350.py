# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0007_auto_20170803_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='casevals',
        ),
        migrations.AddField(
            model_name='case',
            name='casevals',
            field=models.ManyToManyField(related_name='cases', verbose_name=b'Case values', to='dj_experiment.Value'),
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
        migrations.RemoveField(
            model_name='fieldgroup',
            name='fieldnames',
        ),
        migrations.AddField(
            model_name='fieldgroup',
            name='fieldnames',
            field=models.ManyToManyField(related_name='fieldgroups', verbose_name=b'FieldGroup values', to='dj_experiment.Value'),
        ),
        migrations.AlterField(
            model_name='value',
            name='val',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
