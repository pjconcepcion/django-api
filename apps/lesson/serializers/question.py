
from rest_framework import serializers
from apps.lesson.models.question import Question
from apps.lesson.models.choice import Choice

from .choice import ChoiceSerializer

class QuestionSerializer (serializers.ModelSerializer):
  type = serializers.SerializerMethodField()
  choices = ChoiceSerializer(many=True, read_only=True)

  def get_type(self, instance):
    result = len(Choice.objects.filter(questions=instance.id, is_answer=True))
    return "MULTIPLE" if result > 1 else "SINGLE"
  
  class Meta:
    model = Question
    fields = ["id", "lessons", "type", "question_text", "choices"]
