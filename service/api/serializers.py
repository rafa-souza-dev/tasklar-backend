from rest_framework import serializers
from consumer.api.serializers import ConsumerSerializer
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceFullSerializer(serializers.ModelSerializer):
    consumer = ConsumerSerializer()

    class Meta:
        model = Service
        fields = '__all__'
