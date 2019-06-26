from django.db import models


# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
      db_table = "category"