from django.db import models


class Catalog(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=60, null=True, blank=True)
    title = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.brand
