from django.db import models
from authentication.models import User
from tasker.models import Tasker
from service.models import Service

class Assessment(models.Model):
    quality_score = models.IntegerField()
    punctuality_score = models.IntegerField()
    communication_score = models.IntegerField()
    description = models.TextField()
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')
    tasker = models.ForeignKey(Tasker, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def get_average(self):
        return (self.quality_score + self.punctuality_score + self.communication_score) / 3

    def __str__(self):
        return f"Assessment for Consumer #{self.consumer.id} - Tasker #{self.tasker.id}"
