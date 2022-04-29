from django import template
from recipes.models import USER_MODEL, Recipe, ShoppingItem, Ingredient

register = template.Library()


def resize_to(ingredient, target):

    # print(ingredient) this will be equal to 2 cups apples on grandma pie recipe

    servings = ingredient.recipe.servings
    # print(servings) in this case, i put the serving as 3 (not same amount as ingredient amount)
    amount = ingredient.amount
    # print will result in 2 or whatever # was in the ingredient

    if servings is not None and target is not None:
        try:
            ratio = int(target) / int(servings)
            servings = ratio * amount
            # print(servings) suppose to change already
            return servings
        except:
            return amount
            pass

    return amount


register.filter(resize_to)
