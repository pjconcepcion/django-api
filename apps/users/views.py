from rest_framework import viewsets
from rest_framework.decorators import action

from .models.users import Users
from .models.results import Result

from .sequelizers import users, results

class UsersViewSet (viewsets.ModelViewSet):
  queryset = Users.objects.all()
  serializer_class = users.UserSerializer

class ResultsViewSet (viewsets.ModelViewSet):
  queryset = Result.objects.all()
  serializer_class = results.ResultSerializer