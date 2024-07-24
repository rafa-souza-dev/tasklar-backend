from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service.api.filtersets import ServiceFilter
from service.models import Service
from job.models import Job
from tasker.models import Tasker
from authentication.models import User
from .serializers import ServiceFullSerializer, ServiceFullTaskerSerializer, ServiceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class ServiceCreateView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        if not (user_id and job_id and tasker_id):
            return Response({'error': 'User ID, Job ID, or Tasker ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            tasker = Tasker.objects.get(id=tasker_id)
        except Tasker.DoesNotExist:
            return Response({'error': 'Tasker not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Verificar se já existe um serviço com o mesmo user_id, job_id e tasker_id
        if Service.objects.filter(user=user, job=job, tasker=tasker).exists():
            return Response({'error': 'A service with the same User, Job, and Tasker already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'user': user.id,
            'job': job.id,
            'tasker': tasker.id,
            'request_description': request.data.get('request_description'),
            'date': request.data.get('date'),
            'status': request.data.get('status', 'pending'),
            'value': request.data.get('value'),
            'uf': request.data.get('uf'),
            'city': request.data.get('city'),
            'neighborhood': request.data.get('neighborhood')
        }

        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceActionView(APIView):
    def post(self, request, format=None):
        action = request.data.get('action')
        user_id = request.data.get('user_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        valid_actions = ['accept', 'reject']

        if action not in valid_actions:
            return Response({'error': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)

        if not (user_id and job_id and tasker_id):
            return Response({'error': 'User ID, Job ID, or Tasker ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            service = Service.objects.get(user_id=user_id, job_id=job_id, tasker_id=tasker_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found.'}, status=status.HTTP_404_NOT_FOUND)

        if action == 'accept':
            service.status = 'accepted'
        elif action == 'reject':
            service.status = 'rejected'
        
        service.save()
        return Response({'status': f'Service has been {service.status}.'}, status=status.HTTP_200_OK)
    

class ServiceListByJobView(generics.ListAPIView):
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


class ServiceListByTaskerView(generics.ListAPIView):
    serializer_class = ServiceFullSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_queryset(self):
        tasker_id = self.kwargs['tasker_id']
        return Service.objects.filter(tasker_id=tasker_id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceListByConsumerView(generics.ListAPIView):
    serializer_class = ServiceFullTaskerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter

    def get_queryset(self):
        consumer_id = self.kwargs['consumer_id']
        return Service.objects.filter(consumer_id=consumer_id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
