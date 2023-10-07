import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.models.results import Result
from .models.lesson import Lesson
from .models.question import Question
from .models.choice import Choice

from .serializers import lesson, question, choice

class QuestionViewSet (viewsets.ModelViewSet):
  queryset = Question.objects.all();  
  serializer_class = question.QuestionSerializer

class ChoiceViewSet (viewsets.ModelViewSet):
  queryset = Choice.objects.all();  
  serializer_class = choice.ChoiceSerializer

class LessonViewSet (viewsets.ModelViewSet):
  queryset = Lesson.objects.all()
  serializer_class = lesson.LessonSerializer

  @action(
    detail=True, 
    url_path=r"submit",
    methods=["POST"]
  )
  def submit(self, request, pk=None):
    data = request.body
    score = 0
    result = {}

    for question in data:
      answer = data[question]
      choice_results_set = Choice.objects.filter(questions=question, is_answer=True)
      correct_answer = [str(c.id) for c in choice_results_set]

      result[question] = {
        "answers": answer,
        "correct": correct_answer
      }
      if (correct_answer == answer):
        score = score + 1
    
    lesson_model = Lesson.objects.get(pk=pk)
    is_passed = score < lesson_model.passing_score
    context = {
      "score": score,
      "passing_score": lesson_model.passing_score,
      "result": "Fail" if is_passed else "Pass",
      "answers": result
    }

    # result_model = Result(user=None, lesson=lesson_model, score=score, is_passed=is_passed)
    # result_model.save()

    return Response(context)

