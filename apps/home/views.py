from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Population

class HomeView(ListView):
    template_name = 'home/index.html'
    queryset = Population.objects.all()
    paginate_by = 20

class PopulationCreateView(LoginRequiredMixin, CreateView):
    model = Population
    fields = [
        'country',
        'population',
        'yearly_change',
        'net_change',
        'density',
        'land_area',
        'migrants',
        'fert_rate',
        'med_age',
        'urban_pop',
        'world_share',
    ]
    
    def get_success_url(self):
        messages.success(
            self.request, 'A data has been added successfully.')
        return reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = slugify(form.cleaned_data['country'])
        obj.save()
        return super().form_valid(form)


class PopulationUpdateView(LoginRequiredMixin, UpdateView):
    model = Population
    fields = [
        'country',
        'population',
        'yearly_change',
        'net_change',
        'density',
        'land_area',
        'migrants',
        'fert_rate',
        'med_age',
        'urban_pop',
        'world_share',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'A data has been updated successfully.')
        return reverse_lazy("home")


class PopulationDeleteView(LoginRequiredMixin, DeleteView):
    model = Population

    def get_success_url(self):
        messages.success(
            self.request, 'A data has been deleted successfully.')
        return reverse_lazy("home")
