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
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    measure = models.ForeignKey(
        "Measure",
        related_name="measure",
        on_delete=models.PROTECT,
    )
    food = models.ForeignKey(
        "FoodItem",
        related_name="fooditem",
        on_delete=models.PROTECT,
    )
    # possibly add def_str
    def __str__(self):
        return (
            str(self.amount)
            + " "
            + str(self.measure)
            + " "
            + str(self.food)
            + " for "
            + str(self.recipe)
        )


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)
    food_items = models.ManyToManyField("FoodItem", null=True, blank=True)

    def __str__(self):
        return str(self.recipe)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField(
        "Recipe",
        related_name="tags",
    )

    def __str__(self):
        return str(self.name)
