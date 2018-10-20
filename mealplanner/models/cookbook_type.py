from django.db import models


class CookbookType(models.Model):
    # DESSERT = 'Dessert'
    # BREAD = 'Bread'
    # SOUP = 'Soup'
    # SNACK = 'Snack'
    # SALAD = 'Salad'
    # MEAT = 'Meat'
    # MAIN = 'Main Dish'
    # SIDE = 'Side Dish'
    # OTHER = 'Other'
    # APPETIZER = 'Appetizer'
    # CASSEROLE = 'Casserole'

    cookbook_type = models.CharField(max_length=20,
                                     null=True,
                                     unique=True)

    def __str__(self):
        return self.cookbook_type
