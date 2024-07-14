from rest_framework import serializers
from consumer.models import Consumer
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    consumer_id = serializers.PrimaryKeyRelatedField(queryset=Consumer.objects.all(), source='consumer.user.id')
    
    class Meta:
        model = Service
        fields = ('id', 'consumer_id', 'job_id', 'tasker_id', 'request_description', 'date', 'status', 'value', 'uf', 'city', 'neighborhood')
