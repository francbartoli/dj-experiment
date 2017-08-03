# -*- coding: utf-8 -*-

from dj_experiment.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.models import (TimeStampedModel,
                                         TitleSlugDescriptionModel)


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

    def __str__(self):
        """Do a text representation of all models."""

        return "{title}".format(title=self.title)


class Value(TimeStampedModel):
    """Represent values of all cases and fieldgroups."""

    val = models.CharField(blank=False, max_length=100)


class Case(BaseModel):
    """Represent a single case"""

    shortname = models.CharField(blank=False, max_length=50)
    longname = models.CharField(blank=False, max_length=100)
    casevals = models.ForeignKey(Value, related_name='cases')


class FieldGroup(BaseModel):
    """Represent a single group of fields."""

    shortname = models.CharField(blank=False, max_length=50)
    longname = models.CharField(blank=False, max_length=100)
    fieldnames = models.ForeignKey(Value, related_name='fieldgroups')
    is_initialposition = models.BooleanField(default=False)


class Experiment(BaseModel):
    """Represent an experiment."""

    name = models.CharField(max_length=100)
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
