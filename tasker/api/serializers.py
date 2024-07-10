from rest_framework import serializers
from authentication.api.serializers import UserSerializer
from tasker.models import Tasker


class TaskerDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tasker
        fields = '__all__'
