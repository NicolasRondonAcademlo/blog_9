from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email", "is_active", "cellphone")
