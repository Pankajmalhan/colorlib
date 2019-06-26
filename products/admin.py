from django.contrib import admin
from .submodels.category import Category
from .submodels.products import Products
from .submodels.productImages import ProductImages
from .submodels.productCategory import ProductCategory
from .submodels.dealofWeeks import DealsOfWeek
# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ProductImages)
admin.site.register(ProductCategory)
admin.site.register(DealsOfWeek)