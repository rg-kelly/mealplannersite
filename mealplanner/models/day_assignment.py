from django.db import models
from .meal_type import MealType
from .recipe import Recipe


DAY_ASSIGNMENT_TABLE = 'DayAssignment'


class Day (models.Model):
    day = models.CharField(max_length=10,
                           unique=True)
    recipes = models.ManyToManyField(Recipe, through=DAY_ASSIGNMENT_TABLE)

    def __str__(self):
        return self.day


class WeekOfDate (models.Model):
    week_of_date = models.DateField(unique=True)
    recipes = models.ManyToManyField(Recipe, through=DAY_ASSIGNMENT_TABLE)

    def __str__(self):
        return str(self.week_of_date)


class DayAssignment (models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    date = models.ForeignKey(WeekOfDate, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE, null=True, default=1)
