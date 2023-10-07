from django.db import models

from .base_model import BaseModel

class Users (BaseModel, models.Model):
  username = models.CharField(max_length=100)

  def __str__(self):
    return self.username