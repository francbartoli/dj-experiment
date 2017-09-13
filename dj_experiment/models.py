# -*- coding: utf-8 -*-

import os

from dj_experiment.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import (TimeStampedModel,
                                         TitleSlugDescriptionModel)
from taggit.managers import TaggableManager


class BaseModel(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Abstract model to store information about an experiment.

    `title` `description`, and `slug` fields inherited from django-extensions
    TitleSlugDescriptionModel.

    Keyword arguments:
    title - string
    description - string
    slug - string
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """Do a text representation of all models."""
        return "{name}".format(name=self.name)


class Value(TimeStampedModel):
    """Represent values of all cases and fieldgroups."""

    val = models.CharField(blank=False, max_length=100, unique=True)

    def __str__(self):
        """Do a text representation of the model."""
        return "{val}".format(val=self.val)


class Case(BaseModel):
    """Represent a single case of an experiment."""

    shortname = models.CharField(blank=False, max_length=50)
    longname = models.CharField(blank=False, max_length=100)
    casevals = models.ManyToManyField(
        Value, related_name='cases', verbose_name=_('Case values'))


class FieldGroup(BaseModel):
    """Represent a single group of fields."""

    shortname = models.CharField(blank=False, max_length=50)
    longname = models.CharField(blank=False, max_length=100)
    fieldnames = models.ManyToManyField(
        Value, related_name='fieldgroups', verbose_name=_('FieldGroup values'))
    is_initialposition = models.BooleanField(default=False)


class Experiment(BaseModel):
    """Represent an experiment."""

    cases = models.ManyToManyField(
        Case, related_name='experiments', verbose_name=_('Esperiment cases'))
    fieldgroups = models.ForeignKey(FieldGroup, related_name='experiments')
    timeseries = models.BooleanField(default=False)
    data_dir = models.CharField(
        default=settings.DJ_EXPERIMENT_DATA_DIR, max_length=250)
    separator = models.CharField(
        default=settings.DJ_EXPERIMENT_SEPARATOR, max_length=1)
    case_path = models.CharField(default=None, max_length=100)
    initial_position = models.BooleanField(default=False)
    output_prefix = models.CharField(
        default=settings.DJ_EXPERIMENT_OUTPUT_PREFIX, max_length=100)
    output_suffix = models.CharField(
        default=settings.DJ_EXPERIMENT_OUTPUT_SUFFIX, max_length=100)
    validate_data = models.BooleanField(default=True)


class Catalog(BaseModel):
    """Represent a catalog of all experiments."""

    xperiments = models.ManyToManyField(
        Experiment,
        related_name='catalogs',
        verbose_name=_('Catalog experiments'))


class CaseKeyValue(models.Model):
    """Represent a key/value instance of a Case experiment."""

    case = models.ForeignKey(Case)
    value = models.ForeignKey(Value)


class FieldKeyValue(models.Model):
    """Represent a key/value instance of a Field experiment."""

    fieldname = models.ForeignKey(FieldGroup)
    value = models.ForeignKey(Value)


class Dataset(BaseModel):
    """Represent an output dataset for an experiment."""

    dsfilename = models.CharField(
        max_length=256, db_index=True, unique=True)
    dsfile = models.FilePathField(path=os.path.join(
        settings.DJ_EXPERIMENT_BASE_DATA_DIR,
        settings.DJ_EXPERIMENT_DATA_DIR
    ),
        recursive=True,
        max_length=1024)
    tags = TaggableManager()
    casekeyvalues = models.ManyToManyField(
        CaseKeyValue,
        through='CaseBelongingness',
        through_fields=('dataset', 'keyvalue'))
    fieldkeyvalues = models.ManyToManyField(
        FieldKeyValue,
        through='FieldBelongingness',
        through_fields=('dataset', 'keyvalue'))

    def __str__(self):
        return self.dsfilename


class CaseBelongingness(models.Model):
    """Represent bridge to a key,value case for a dataset of an experiment."""

    dataset = models.ForeignKey(Dataset)
    keyvalue = models.ForeignKey(CaseKeyValue)


class FieldBelongingness(models.Model):
    """Represent bridge to a key,value field for a dataset of an experiment."""

    dataset = models.ForeignKey(Dataset)
    keyvalue = models.ForeignKey(FieldKeyValue)
