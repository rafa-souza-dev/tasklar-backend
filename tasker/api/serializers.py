from rest_framework import serializers
from assessments.models import Assessment
from authentication.api.serializers import UserSerializer
from tasker.models import Tasker


class TaskerDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rating = serializers.SerializerMethodField()


    class Meta:
        model = Tasker
        fields = '__all__'

    def get_rating(self, tasker):
        assessments = Assessment.objects.filter(tasker=tasker)
        
        if not assessments.exists():
            return 0

        total_average = sum([assessment.get_average() for assessment in assessments])
        average_rating = total_average / assessments.count()

        return average_rating
