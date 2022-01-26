from re import T
from statistics import mode
from tkinter.ttk import Widget
from typing_extensions import Required
from django.db import models
from datetime import datetime

class FeedbackModel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    post_time = models.DateTimeField(blank=True,default=datetime.now())

    def __str__(self):
        return self.name