from django.db import models


class Unit (models.Model):
    unit = models.CharField(max_length=20,
                            unique=True)
    is_plural = models.BooleanField()
    match_unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, related_name='match', null=True, blank=True)

    def __str__(self):
        return self.unit
