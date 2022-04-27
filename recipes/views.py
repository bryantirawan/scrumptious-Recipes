from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User

USER_MODEL = settings.AUTH_USER_MODEL


from recipes.forms import RatingForm


# from recipes.forms import RecipeForm
from recipes.models import USER_MODEL, Recipe


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
                return redirect("recipe_detail", pk=recipe_id)
            except Recipe.DoesNotExist:
                return redirect("recipes_list")


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2


class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "recipes/users.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")
