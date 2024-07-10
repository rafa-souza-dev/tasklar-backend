from django.db import models
from tasker.models import Tasker


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    tasker = models.ForeignKey(Tasker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    contact = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    duration = models.CharField(max_length=255)
    days_of_week = models.CharField(max_length=7, help_text='Dias da semana em que o serviço está disponível. Exemplo: "0123456"')
    start_time = models.TimeField(help_text='Horário de início de atendimento')
    end_time = models.TimeField(help_text='Horário de fim de atendimento')

    def set_days_of_week(self, days):
        self.days_of_week = ''.join(['1' if day else '0' for day in days])

    def get_days_of_week(self):
        return [day == '1' for day in self.days_of_week]

    def __str__(self):
        return f'{self.tasker.user.email} - {self.category.name}'
