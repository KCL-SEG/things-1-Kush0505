from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class things(models.Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()

