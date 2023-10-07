from rest_framework import serializers
from apps.users.models.users import Users

class UserSerializer (serializers.ModelSerializer):

  class Meta:
    model = Users
    exclude = ["updated_at", "created_at", "password"]