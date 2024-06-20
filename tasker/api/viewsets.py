from rest_framework import viewsets

from .serializers import PeriodSerializer, CategorySerializer
from ..models import Period, Category

class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
