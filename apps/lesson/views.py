from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.models.results import Result
from apps.users.models.users import Users

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

  def get_result(self, object):
    print(object)
    return 

class LessonViewSet (viewsets.ModelViewSet):
  parser_classes = [JSONParser]
  queryset = Lesson.objects.all()
  serializer_class = lesson.LessonSerializer

  @action(
    detail=True, 
    url_path=r"submit",
    methods=["POST"]
  )
  def submit(self, request, pk=None):
    data = request.data
    score = 0

    for question in data['answers']:
      answer = data['answers'][question]
      choice_results_set = Choice.objects.filter(questions=question, is_answer=True)
      correct_answer = [str(c.id) for c in choice_results_set]
      if (correct_answer == answer):
        score = score + 1
    
    lesson_model = Lesson.objects.get(pk=pk)
    is_passed = score < lesson_model.passing_score
    context = {
      "score": score,
      "passing_score": lesson_model.passing_score,
      "result": "Fail" if is_passed else "Pass"
    }

    user = Users.objects.get_or_create(username=data['username'])
    result_model = Result(user=user[0], lesson=lesson_model, score=score, is_passed=is_passed)
    result_model.save()

    return Response(context)

