from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=10)
    addr = models.CharField(max_length=50)
