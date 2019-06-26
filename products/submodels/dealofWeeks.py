from django.db import models
from .products import Products

class DealsOfWeek(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    class Meta:
        db_table = "dealsOfWeek"