from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service.api.serializers import ServiceSerializer
from job.models import Job
from tasker.models import Tasker
from consumer.models import Consumer

class ServiceCreateView(APIView):
    def post(self, request, format=None):
       
        consumer_id = request.data.get('consumer_id')
        job_id = request.data.get('job_id')

        
        if not consumer_id or not job_id:
            return Response({'error': 'Consumer ID or Job ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        
        try:
            job = Job.objects.get(id=job_id)
            tasker_id = job.tasker_id
        except Job.DoesNotExist:
            return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

      
        data = {
            'consumer_id': consumer_id,
            'job_id': job_id,
            'tasker_id': tasker_id,
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
