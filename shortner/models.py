from django.db import models


# Create your models here.

class Url(models.Model):
    uuid = models.CharField(max_length=10)
    link = models.CharField(max_length=10000)

