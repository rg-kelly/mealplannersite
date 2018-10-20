from django.db import models


class MealType (models.Model):
    # DINNER = 'Dinner'
    # LUNCH = 'Lunch'
    # BREAKFAST = 'Breakfast'
    # SNACK = 'Snack'

    meal_type = models.CharField(max_length=10,
                                 blank=False,
                                 unique=True)

    def __str__(self):
        return self.meal_type
