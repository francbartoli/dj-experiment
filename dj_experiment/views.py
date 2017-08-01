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
	FieldGroup,
    Value,
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


class FieldGroupCreateView(CreateView):

    model = FieldGroup


class FieldGroupDeleteView(DeleteView):

    model = FieldGroup


class FieldGroupDetailView(DetailView):

    model = FieldGroup


class FieldGroupUpdateView(UpdateView):

    model = FieldGroup


class FieldGroupListView(ListView):

    model = FieldGroup


class ValueCreateView(CreateView):

    model = Value


class ValueDeleteView(DeleteView):

    model = Value


class ValueDetailView(DetailView):

    model = Value


class ValueUpdateView(UpdateView):

    model = Value


class ValueListView(ListView):

    model = Value


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
