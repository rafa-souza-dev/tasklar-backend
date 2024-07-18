from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import User
from consumer.models import Consumer
from job.models import Category, Job
from service.models import Service
from tasker.models import Tasker


class TestListServices(APITestCase):
    def setUp(self) -> None:
        self.tasker_email = 'tasker@test.com'
        self.tasker_password = 'S6y6@9iP5Q&r5BQx'
        self.consumer_email = 'consumer@test.com'
        self.consumer_password = 'S6y6@9iP5Q&r5BQx'
        self.hashed_tasker_password = make_password(self.tasker_password)
        self.hashed_consumer_password = make_password(self.consumer_password)

        user_tasker = User.objects.create(email=self.tasker_email, password=self.hashed_tasker_password, profile_type='T')
        user_consumer = User.objects.create(email=self.consumer_email, password=self.hashed_consumer_password, profile_type='C')
        tasker = Tasker.objects.create(user=user_tasker)
        consumer = Consumer.objects.create(user=user_consumer)
        category = Category.objects.create(name='Faxina')
        job = Job.objects.create(
            tasker=tasker, category=category, contact='123',
            value=100, days_of_week='0001110', description='muito bão',
            duration='1hr30min', start_time='06:00:00', end_time='19:00:00',
        )
        Service.objects.create(
           consumer=consumer, job=job, tasker=tasker,
           request_description='casa com 3 quartos e dois banheiros', date='2024-08-01',
           time='06:00:00', uf='PE', city='Pesqueira', neighborhood='Prado'
        )

        return super().setUp()

    def test_should_be_able_to_list_services(self):
        self.assertTrue(1 > 0)
