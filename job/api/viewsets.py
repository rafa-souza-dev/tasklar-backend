from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from job.api.filtersets import JobFilterSet
from .serializers import CategorySerializer, JobDetailsSerializer, JobListSerializer, JobSerializer
from job.models import Category, Job

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = None

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]

class JobCreateAPIView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilterSet

class JobRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailsSerializer
