from statistics import mode
from django.db import models

# Create your models here.
class ShortSummary(models.Model):
    description = models.CharField(max_length = 400)
    employment_status = models.CharField(max_length = 100)

    def __str__(self):
        return "Index"