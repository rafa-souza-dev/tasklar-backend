from rest_framework import serializers

from ..models import Tasker, Period, Category
from authentication.models import User


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TaskerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class TaskerListSerializer(serializers.ModelSerializer):
    user = TaskerUserSerializer(read_only=True)
    category = CategorySerializer()
    periods = PeriodSerializer(many=True)

    class Meta:
        model = Tasker
        fields = ('id', 'user', 'category', 'periods', 'phone', 'hourly_rate', 'description')


class TaskerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasker
        fields = ('id', 'category', 'periods', 'phone', 'hourly_rate', 'description')
