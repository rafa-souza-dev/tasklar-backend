from rest_framework import serializers
from job.models import Job
from tasker.models import Tasker

class JobSerializer(serializers.ModelSerializer):
    days_of_week = serializers.ListField(
        child=serializers.BooleanField(), write_only=True
    )
    days_of_week_display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

    def get_days_of_week_display(self, obj):
        return obj.get_days_of_week()

    def create(self, validated_data):
        days_of_week = validated_data.pop('days_of_week')
        job = Job.objects.create(**validated_data)
        job.set_days_of_week(days_of_week)
        job.save()
        return job

    def update(self, instance, validated_data):
        days_of_week = validated_data.pop('days_of_week', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if days_of_week is not None:
            instance.set_days_of_week(days_of_week)
        instance.save()
        return instance