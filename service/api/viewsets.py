from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from consumer.models import Consumer
from service.api.filtersets import ServiceFilter
from service.models import Service
from job.models import Job
from tasker.models import Tasker
from .serializers import ServiceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class ServiceCreateView(APIView):
    serializer_class = ServiceSerializer

    def post(self, request, format=None):
        consumer_id = request.data.get('consumer_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        if not (consumer_id and job_id and tasker_id):
            return Response({'error': 'Consumer ID, Job ID, or Tasker ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            consumer = Consumer.objects.get(id=consumer_id)
        except User.DoesNotExist:
            return Response({'error': 'Consumer not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            tasker = Tasker.objects.get(id=tasker_id)
        except Tasker.DoesNotExist:
            return Response({'error': 'Tasker not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'consumer': consumer.id,
            'job': job.id,
            'tasker': tasker.id,
            'request_description': request.data.get('request_description'),
            'date': request.data.get('date'),
            'status': request.data.get('status', 'pending'),
            'uf': request.data.get('uf'),
            'city': request.data.get('city'),
            'neighborhood': request.data.get('neighborhood'),
            'time': request.data.get('time'),
        }

        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceActionView(APIView):
    def post(self, request, format=None):
        action = request.data.get('action')
        consumer_id = request.data.get('consumer_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        valid_actions = ['accept', 'reject']

        if action not in valid_actions:
            return Response({'error': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)

        if not (consumer_id and job_id and tasker_id):
            return Response({'error': 'Consumer ID, Job ID, or Tasker ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            service = Service.objects.get(consumer_id=consumer_id, job_id=job_id, tasker_id=tasker_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found.'}, status=status.HTTP_404_NOT_FOUND)

        if action == 'accept':
            service.status = 'accepted'
        elif action == 'reject':
            service.status = 'rejected'
        
        service.save()
        return Response({'status': f'Service has been {service.status}.'}, status=status.HTTP_200_OK)
    

class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Service.objects.filter(job_id=job_id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) 