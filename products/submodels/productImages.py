from django.db import models
from .products import Products

class ProductImages(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    class Meta:
        db_table = "productImage"