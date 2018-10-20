from django.db import models
from .unit import Unit
from .store import Store
from .ingredient import Ingredient
from .day_assignment import WeekOfDate


class Purchase (models.Model):
    price_per_unit = models.FloatField()
    amount = models.FloatField(null=True,
                               blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    date = models.ForeignKey(WeekOfDate, on_delete=models.CASCADE)
    on_sale = models.BooleanField(null=False,
                                  blank=False,
                                  default=False)
    notes = models.CharField(max_length=200,
                             null=True,
                             blank=True)
