from re import template
from typing import List
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from mealplans.models import USER_MODEL, MealPlan

USER_MODEL = settings.AUTH_USER_MODEL


# Create your views here.
class MealPlanListView(ListView):
    model = MealPlan
    context_object_name = "mealplans"
    template_name = "mealplans/list.html"
    paginate_by = 2

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(DetailView):
    model = MealPlan
    context_object_name = "mealplans"
    template_name = "mealplans/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "mealplans/new.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("mealplans_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    context_object_name = "mealplans"
    template_name = "mealplans/edit.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("mealplans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    context_object_name = "mealplans"
    template_name = "mealplans/delete.html"
    success_url = reverse_lazy("mealplans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
