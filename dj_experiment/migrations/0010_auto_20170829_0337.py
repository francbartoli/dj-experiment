# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_experiment', '0009_auto_20170804_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseBelongingness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseKeyValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case', models.ForeignKey(to='dj_experiment.Case')),
                ('value', models.ForeignKey(to='dj_experiment.Value')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dj_experiment.BaseModel')),
                ('dsfilename', models.CharField(unique=True, max_length=256, db_index=True)),
                ('dsfile', models.FilePathField(path='./', max_length=1024, recursive=True)),
                ('casekeyvalues', models.ManyToManyField(to='dj_experiment.CaseKeyValue', through='dj_experiment.CaseBelongingness')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=('dj_experiment.basemodel',),
        ),
        migrations.CreateModel(
            name='FieldBelongingness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataset', models.ForeignKey(to='dj_experiment.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='FieldKeyValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fieldname', models.ForeignKey(to='dj_experiment.FieldGroup')),
                ('value', models.ForeignKey(to='dj_experiment.Value')),
            ],
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='name',
            field=models.CharField(unique=True, max_length=255),
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
        migrations.AddField(
            model_name='fieldbelongingness',
            name='keyvalue',
            field=models.ForeignKey(to='dj_experiment.FieldKeyValue'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='fieldkeyvalues',
            field=models.ManyToManyField(to='dj_experiment.FieldKeyValue', through='dj_experiment.FieldBelongingness'),
        ),
        migrations.AddField(
            model_name='casebelongingness',
            name='dataset',
            field=models.ForeignKey(to='dj_experiment.Dataset'),
        ),
        migrations.AddField(
            model_name='casebelongingness',
            name='keyvalue',
            field=models.ForeignKey(to='dj_experiment.CaseKeyValue'),
        ),
    ]
