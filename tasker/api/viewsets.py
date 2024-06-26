from rest_framework import viewsets, generics

from .serializers import PeriodSerializer, CategorySerializer, TaskerSerializer
from ..models import Period, Category, Tasker

class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskerListView(generics.ListAPIView):
    serializer_class = TaskerSerializer
    queryset = Tasker.objects.all()
