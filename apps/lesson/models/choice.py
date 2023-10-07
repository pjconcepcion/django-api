from django.db import models

from .base_model import BaseModel
from .question import Question

class Choice (BaseModel, models.Model):
  questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
  choice_text = models.CharField("choice", max_length=100)
  is_answer = models.BooleanField("is answer", default=False)

  def __str__(self):
    return self.choice_text