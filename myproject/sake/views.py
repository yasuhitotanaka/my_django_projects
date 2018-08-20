# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)
from django.shortcuts import render

from sake.models import SakeModel,SakeTypeModel,MakerModel
from sake.forms import SakeForm,SakeTypeForm,MakerForm


class SakeListView(ListView):
    model = SakeModel
    template_name = 'list.html'

    def get_queryset(self):
        return SakeModel.objects.order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = {'sakes':self.get_queryset()}
        return context


class SakeDetailView(DetailView):
    model = SakeModel
    template_name = 'detail.html'


class SakeCreatelView(CreateView):
    model = SakeModel
    form_class =SakeForm
    template_name = 'create.html'


class SakeTypeCreatelView(CreateView):
    model = SakeTypeModel
    form_class =SakeTypeForm
    template_name = 'type_create.html'


class MakerCreateView(CreateView):
    model = MakerModel
    form_class =MakerForm
    template_name = 'maker_create.html'


class MakerListView(ListView):
    model = MakerModel
    template_name = 'maker_list.html'

    def get_queryset(self):
        return MakerModel.objects.order_by('-name')

    def get_context_data(self, **kwargs):
        context = {'makers':self.get_queryset()}
        return context