from statistics import mode
from tkinter.ttk import Widget
from django.db import models


class FeedbackModel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    

    def __str__(self):
        return self.name
