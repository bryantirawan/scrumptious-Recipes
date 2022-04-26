from django.urls import path

from tags.views import (
    TagDeleteView,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagUpdateView,
)

urlpatterns = [
    path("", TagListView.as_view(), name="tags_list"),
    path("<int:pk>/", TagDetailView.as_view(), name="tag_detail"),
    path("new/", TagCreateView.as_view(), name="tag_new"),
    path("<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
    path("<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
