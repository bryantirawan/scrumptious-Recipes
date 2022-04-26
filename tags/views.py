from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
# def show_tags(request):
#     context = {
#         "tags": Tag.objects.all() if Tag else None,
#     }
#     return render(request, "tags/list.html", context)


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/list.html"
    paginate_by = 3


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/detail.html"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")
