from rest_framework import serializers

from authentication import models
from tasker.api.serializers import TaskerCreateSerializer

class UserSerializer(serializers.ModelSerializer):
    tasker = TaskerCreateSerializer(required=False)
    password = serializers.CharField(write_only=True, max_length=16)

    class Meta:
        model = models.User
        fields = ('id', 'name', 'email', 'uf', 'city', 'password', 'tasker')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
