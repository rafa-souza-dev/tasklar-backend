from rest_framework import serializers
from assessments.models import Assessment
from authentication.models import User
from tasker.models import Tasker
from service.models import Service

class AssessmentSerializer(serializers.ModelSerializer):
    consumer_id = serializers.IntegerField()
    tasker_id = serializers.IntegerField()
    service_id = serializers.IntegerField()

    class Meta:
        model = Assessment
        fields = [
            'quality_score',
            'punctuality_score',
            'communication_score',
            'description',
            'consumer_id',
            'tasker_id',
            'service_id'
        ]

        
