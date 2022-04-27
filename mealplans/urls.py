from django.urls import path

from mealplans.views import (
    MealPlanListView,
    MealPlanDetailView,
    MealPlanCreateView,
    MealPlanUpdateView,
    MealPlanDeleteView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mealplans_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="mealplan_detail"),
    path("new/", MealPlanCreateView.as_view(), name="mealplan_new"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mealplan_edit"),
    path(
        "<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mealplan_delete"
    ),
]
