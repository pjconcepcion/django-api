from rest_framework import serializers
from apps.lesson.models.lesson import Lesson

from .question import QuestionSerializer
from apps.users.sequelizers.results import ResultSerializer

class LessonSerializer (serializers.ModelSerializer):
  question = QuestionSerializer(many=True, read_only=True)
  results = ResultSerializer(many=True,  read_only=True)

  class Meta:
    model = Lesson
    exclude = ["updated_at", "created_at"]