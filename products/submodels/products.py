from django.db import models
from .category import Category
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    

class Products(models.Model):
    title = models.CharField(max_length=250)
    availibility = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/',default='img/noproduct.png')
    actualPrice = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    offerPrice = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1200,default='')
    width = models.IntegerField(help_text="value in mm")
    height = models.IntegerField(help_text="value in mm")
    depth = models.IntegerField(help_text="value in mm")
    weight = models.IntegerField(help_text="value in gm")
    qualityCheck = models.BooleanField(default=True)
    created_on=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"
