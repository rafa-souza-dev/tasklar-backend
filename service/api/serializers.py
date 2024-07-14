from rest_framework import serializers
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'user', 'job', 'tasker', 'request_description', 'date', 'status', 'value', 'uf', 'city', 'neighborhood')