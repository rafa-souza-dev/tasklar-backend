from rest_framework import serializers
from consumer.api.serializers import ConsumerSerializer
from job.api.serializers import JobDetailsCategorySerializer
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceFullSerializer(serializers.ModelSerializer):
    consumer = ConsumerSerializer()
    job = JobDetailsCategorySerializer()

    class Meta:
        model = Service
        fields = '__all__'
