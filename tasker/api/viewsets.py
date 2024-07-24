from rest_framework import status as drf_status
from rest_framework.response import Response
from rest_framework.views import APIView
from service.models import Service
from tasker.api.serializers import TaskerDetailsSerializer
from tasker.models import Tasker

class TaskerServiceActionView(APIView):
    def post(self, request, format=None):
        service_id = request.data.get('service_id')
        service_status = request.data.get('status')
        consumer_id = request.data.get('consumer_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        valid_statuses = ['accept', 'reject']

        if service_status not in valid_statuses:
            return Response({'error': 'Invalid status.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        if not (service_id and consumer_id and job_id and tasker_id):
            return Response({'error': 'Service ID, User ID, Job ID, or Tasker ID not provided.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        try:
            service = Service.objects.get(id=service_id, consumer_id=consumer_id, job_id=job_id, tasker_id=tasker_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found.'}, status=drf_status.HTTP_404_NOT_FOUND)

        if service.status != 'pending':
            return Response({'error': f'Cannot {service_status} a service that is not pending.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        if service_status == 'accept':
            service.status = 'accepted'
        elif service_status == 'reject':
            service.status = 'rejected'
        
        service.save()
        return Response({'status': f'Service has been {service.status}.'}, status=drf_status.HTTP_200_OK)
        
class TaskerDetailView(APIView):
    def get(self, request, tasker_id, format=None):
        try:
            tasker = Tasker.objects.get(id=tasker_id)
        except Tasker.DoesNotExist:
            return Response({'error': 'Tasker not found.'}, status=drf_status.HTTP_404_NOT_FOUND)

        serializer = TaskerDetailsSerializer(tasker)
        return Response(serializer.data, status=drf_status.HTTP_200_OK)