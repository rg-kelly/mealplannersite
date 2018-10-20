from django.db import models


class RecipeType (models.Model):
    # MAIN = 'Main'
    # SIDE = 'Side'

    recipe_type = models.CharField(max_length=10,
                                   blank=False,
                                   unique=True)

    def __str__(self):
        return self.recipe_type
