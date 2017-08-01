# -*- coding: utf-8 -*-

from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class BaseModel(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Abstract model to store information about an experiment that may or
    may not be given.
    `title` `description`, and `slug` fields inherited from django-extensions
    TitleSlugDescriptionModel.
    """

    def __str__(self):
        return "{title}".format(title=self.title)


class Experiment(BaseModel):
    pass


class Case(BaseModel):
    pass


class FieldGroup(BaseModel):
    pass


class Value(TimeStampedModel):
    pass


class Catalog(BaseModel):
    pass
