from rest_framework import serializers
from assessments.models import Assessment
from authentication.models import User
from tasker.models import Tasker
from service.models import Service

class AssessmentSerializer(serializers.ModelSerializer):
    consumer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='consumer.id')
    tasker = serializers.PrimaryKeyRelatedField(queryset=Tasker.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Assessment
        fields = '__all__'
