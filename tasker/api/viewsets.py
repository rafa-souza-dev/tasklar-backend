from rest_framework import status as drf_status
from rest_framework.response import Response
from rest_framework.views import APIView
from service.models import Service

class TaskerServiceActionView(APIView):
    def post(self, request, format=None):
        service_id = request.data.get('service_id')
        service_status = request.data.get('status')
        user_id = request.data.get('user_id')
        job_id = request.data.get('job_id')
        tasker_id = request.data.get('tasker_id')

        valid_statuses = ['accept', 'reject']

        if service_status not in valid_statuses:
            return Response({'error': 'Invalid status.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        if not (service_id and user_id and job_id and tasker_id):
            return Response({'error': 'Service ID, User ID, Job ID, or Tasker ID not provided.'}, status=drf_status.HTTP_400_BAD_REQUEST)

        try:
            service = Service.objects.get(id=service_id, user_id=user_id, job_id=job_id, tasker_id=tasker_id)
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