from django.db import models
from .products import Products

class DealsOfWeek(models.Model):
    product=models.OneToOneField(Products,on_delete=models.CASCADE,unique=True)
    class Meta:
        db_table = "dealsOfWeek"