from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import JobSerializer
from job.models import Job

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = None  # Atualize conforme necessário

class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
