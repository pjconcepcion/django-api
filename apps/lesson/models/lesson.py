from django.db import models

from .base_model import BaseModel

class Lesson (BaseModel, models.Model):
  title = models.CharField(max_length=100, default="title")
  content = models.CharField(max_length=200)
  passing_score = models.IntegerField(default=0)
  
  def __str__(self):
    return self.content