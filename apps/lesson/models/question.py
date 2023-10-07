from django.db import models

from .lesson import Lesson
from .base_model import BaseModel

class Question (BaseModel, models.Model):

  lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="question")
  question_text = models.CharField("question", max_length=200)

  def __str__(self):
    return self.question_text