from django.db import models
from django.utils import timezone

class BaseModel (models.Model):
  created_at = models.DateTimeField("created at", default=timezone.now)
  updated_at = models.DateTimeField("updated at", default=timezone.now)