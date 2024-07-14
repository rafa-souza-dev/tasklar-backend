from django.db import models
from job.models import Job
from tasker.models import Tasker
from consumer.models import Consumer  

class Service(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tasker = models.ForeignKey(Tasker, on_delete=models.CASCADE)
    request_description = models.TextField()
    date = models.DateField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('in_progress', 'In Progress'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    value = models.DecimalField(max_digits=11, decimal_places=2)
    uf = models.CharField(max_length=2)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)

    def __str__(self):
        return f"Service #{self.id} - {self.request_description}"
