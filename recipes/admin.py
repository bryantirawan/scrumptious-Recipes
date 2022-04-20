from django.contrib import admin

from recipes.models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin): 
    pass

admin.site.register(Recipe, RecipeAdmin)