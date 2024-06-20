from rest_framework import serializers

from ..models import Tasker, Period, Category

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TaskerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasker
        fields = ('id', 'category', 'periods', 'phone', 'hourly_rate', 'description')
