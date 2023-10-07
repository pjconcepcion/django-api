from rest_framework import serializers
from apps.users.models.results import Result

from .users import UserSerializer

class ResultSerializer (serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Result
    exclude = ["updated_at", "created_at"]