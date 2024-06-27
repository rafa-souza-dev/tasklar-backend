from rest_framework import viewsets, generics

from .serializers import (
    PeriodSerializer, CategorySerializer, TaskerCreateSerializer,
    TaskerListSerializer, TaskerRetrieveSerializer
)
from ..models import Period, Category, Tasker

class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskerListView(generics.ListAPIView):
    serializer_class = TaskerListSerializer
    queryset = Tasker.objects.all()


class TaskerCreateView(generics.CreateAPIView):
    serializer_class = TaskerCreateSerializer
    queryset = Tasker.objects.all()


class TaskerRetrieveView(generics.RetrieveAPIView):
    serializer_class = TaskerRetrieveSerializer
    queryset = Tasker.objects.all()
