from django.db import models

# Create your models here.
class Drink(models ):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)