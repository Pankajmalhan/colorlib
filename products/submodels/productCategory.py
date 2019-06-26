from django.db import models
from .products import Products
from .category import Category


class ProductCategory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "productCategory"
        unique_together = ('product', 'category')
