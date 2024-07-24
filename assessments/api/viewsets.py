from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from assessments.models import Assessment
from tasker.models import Tasker
from service.models import Service
from .serializers import AssessmentSerializer

class AssessmentCreateView(APIView):
    def post(self, request, format=None):
        data = request.data.copy()

        consumer_id = data.get('consumer_id')
        tasker_id = data.get('tasker_id')
        service_id = data.get('service_id')

        # Verifique se a avaliação já existe para o mesmo consumidor, tasker e serviço
        if Assessment.objects.filter(consumer_id=consumer_id, tasker_id=tasker_id, service_id=service_id).exists():
            return Response({'error': 'Você já avaliou este serviço.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AssessmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
