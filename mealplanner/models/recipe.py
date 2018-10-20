from django.db import models
from .recipe_type import RecipeType
from .cookbook_type import CookbookType
from .ingredient import Ingredient
from .unit import Unit


class Recipe (models.Model):
    RECIPE_ELEMENT_TABLE = 'RecipeElement'
    recipe_name = models.CharField(max_length=200,
                                   unique=True)
    recipe_instructions = models.TextField(null=True,
                                           blank=True)
    preparation_time_minutes = models.FloatField(null=True,
                                                 blank=True)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.SET_DEFAULT, default=1)
    cookbook_type = models.ForeignKey(CookbookType, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through=RECIPE_ELEMENT_TABLE)

    def __str__(self):
        return self.recipe_name


class RecipeElement (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
