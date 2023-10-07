from rest_framework import serializers
from apps.lesson.models.choice import Choice

class ChoiceSerializer (serializers.ModelSerializer):
  class Meta:
    model = Choice
    exclude = ["updated_at", "created_at"]
    extra_kwargs = { "is_answer" : { "write_only": True }}
