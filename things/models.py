from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


# Create your models here.

class things(models.Model):
    name = models.CharField( max_length = 30, blank = False, unique = True)
    description = models.CharField(max_length = 30, blank = False, unique = True)
    quantity = models.IntegerField(unique = False, default = 0, validators = [MinValueValidator(0, message = "Value must be greater than or equal to 0"), MaxValueValidator(100, message = "Value must be less than or equal to 100")])

