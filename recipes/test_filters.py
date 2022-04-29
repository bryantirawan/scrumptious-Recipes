from re import A
from unittest import TestCase
from recipes.models import Recipe, Ingredient
from recipes.templatetags.resizer import resize_to


class ResizeToTests(TestCase):
    def test_error_when_ingredient_is_none(self):
        with self.assertRaises(AttributeError):
            resize_to(None, 3)

    def test_recipe_has_no_serving(self):
        recipe = Recipe(servings=None)
        ingredient = Ingredient(recipe=recipe, amount=5)
        result = resize_to(ingredient, None)
        self.assertEqual(5, result)

    def test_recipe_has_no_serving_two(self):
        recipe = Recipe(servings=None)
        ingredient = Ingredient(recipe=recipe, amount=5)
        result = resize_to(ingredient, 6)
        self.assertEqual(5, result)

    def test_resize_to_is_none(self):
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        result = resize_to(ingredient, None)
        self.assertEqual(5, result)

    def test_target_is_string(self):
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)
        result = resize_to(ingredient, "abc")
        self.assertEqual(5, result)
