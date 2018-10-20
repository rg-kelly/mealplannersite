from django.db import models


class Store (models.Model):
    store = models.CharField(max_length=100,
                             unique=True)

    def __str__(self):
        return self.store
