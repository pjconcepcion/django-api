from rest_framework import serializers
from apps.lesson.models.choice import Choice
from apps.lesson.models.question import Question

class ChoiceSerializer (serializers.ModelSerializer):
  class Meta:
    model = Choice
    exclude = ["updated_at", "created_at"]
