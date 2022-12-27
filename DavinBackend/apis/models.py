from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 180)
    age = models.CharField(max_length = 180)
    gender = models.CharField(max_length = 180)
    locality = models.CharField(max_length = 180)