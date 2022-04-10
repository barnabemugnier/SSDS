from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.fields.CharField(max_length=100)

    