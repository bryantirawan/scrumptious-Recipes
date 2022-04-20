from tkinter import CASCADE
from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        Recipe,
        related_name="recipe",
        on_delete=models.CASCADE,
    )
    measure = models.ForeignKey(
        Measure,
        related_name="measure",
        on_delete=models.PROTECT,
    )
    food = models.ForeignKey(
        FoodItem,
        related_name="fooditem",
        on_delete=models.PROTECT,
    )
    # possibly add def_str
    def __str__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)

    def __str__(self):
        return self.name
