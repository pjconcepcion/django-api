from django.db import models

from .base_model import BaseModel

class Users (BaseModel, models.Model):
  name = models.CharField(max_length=200)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return self.name