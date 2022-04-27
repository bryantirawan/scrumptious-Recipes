from django.contrib import admin

from mealplans.models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    pass


# Register your models here.

admin.site.register(MealPlan, MealPlanAdmin)
