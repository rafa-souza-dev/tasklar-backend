from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from assessments.models import Assessment
from authentication.models import User
from tasker.models import Tasker
from service.models import Service
from .serializers import AssessmentSerializer

class AssessmentCreateView(APIView):
    def post(self, request, format=None):
        consumer_id = request.data.get('consumer_id')

        if not consumer_id:
            return Response({'error': 'Consumer ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            consumer = User.objects.get(id=consumer_id)
        except User.DoesNotExist:
            return Response({'error': 'Consumer not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        serializer = AssessmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
