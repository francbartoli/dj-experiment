# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Experiment,
	Case,
	Field,
	Catalog,
)


class ExperimentCreateView(CreateView):

    model = Experiment


class ExperimentDeleteView(DeleteView):

    model = Experiment


class ExperimentDetailView(DetailView):

    model = Experiment


class ExperimentUpdateView(UpdateView):

    model = Experiment


class ExperimentListView(ListView):

    model = Experiment


class CaseCreateView(CreateView):

    model = Case


class CaseDeleteView(DeleteView):

    model = Case


class CaseDetailView(DetailView):

    model = Case


class CaseUpdateView(UpdateView):

    model = Case


class CaseListView(ListView):

    model = Case


class FieldCreateView(CreateView):

    model = Field


class FieldDeleteView(DeleteView):

    model = Field


class FieldDetailView(DetailView):

    model = Field


class FieldUpdateView(UpdateView):

    model = Field


class FieldListView(ListView):

    model = Field


class CatalogCreateView(CreateView):

    model = Catalog


class CatalogDeleteView(DeleteView):

    model = Catalog


class CatalogDetailView(DetailView):

    model = Catalog


class CatalogUpdateView(UpdateView):

    model = Catalog


class CatalogListView(ListView):

    model = Catalog

