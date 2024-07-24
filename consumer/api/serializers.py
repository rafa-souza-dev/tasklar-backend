from rest_framework import serializers
from authentication.api.serializers import UserSerializer
from consumer.models import Consumer


class ConsumerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Consumer
        fields = '__all__'
