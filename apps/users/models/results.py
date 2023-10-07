from django.db import models

from .base_model import BaseModel
from .users import Users
from apps.lesson.models.lesson import Lesson

class Result (BaseModel, models.Model):
  user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user")
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="results")
  score = models.IntegerField()
  is_passed = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.lesson} - {self.score}'