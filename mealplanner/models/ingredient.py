from django.db import models


class Ingredient (models.Model):
    ingredient_name = models.CharField(max_length=200,
                                       unique=True)

    def __str__(self):
        return self.ingredient_name
