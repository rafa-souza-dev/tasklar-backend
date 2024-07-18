from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase
import urllib.parse

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
        self.job = Job.objects.create(
            tasker=tasker, category=category, contact='123',
            value=100, days_of_week='0001110', description='muito bão',
            duration='1hr30min', start_time='06:00:00', end_time='19:00:00',
        )
        Service.objects.create(
           consumer=consumer, job=self.job, tasker=tasker,
           request_description='casa com 3 quartos e dois banheiros', date='2024-08-01',
           time='06:00:00', uf='PE', city='Pesqueira', neighborhood='Baixa Grande'
        )
        Service.objects.create(
           consumer=consumer, job=self.job, tasker=tasker,
           request_description='casa com 3 quartos e dois banheiros', date='2024-10-10',
           time='06:00:00', uf='PE', city='Pesqueira', neighborhood='Prado', status='accepted'
        )

        return super().setUp()

    def test_should_be_able_to_list_services(self):
        url = reverse('job-services', kwargs={'job_id': self.job.id})

        response = self.client.get(
            url,
            format='json',
        )

        json_response = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 2)
        self.assertEqual(json_response[0]['date'], '2024-08-01')
        self.assertEqual(json_response[0]['time'], '06:00:00')

    def test_should_not_be_able_to_list_services_from_nonexistent_job(self):
        url = reverse('job-services', kwargs={'job_id': 400})

        response = self.client.get(
            url,
            format='json',
        )

        json_response = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 0)

    def test_should_be_able_to_list_services_filtered_by_date(self):
        url = reverse('job-services', kwargs={'job_id': self.job.id})
        url_with_query = f"{url}?date=2024-08-01"

        response = self.client.get(
            url_with_query,
            format='json',
        )

        json_response = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['date'], '2024-08-01')
        self.assertEqual(json_response[0]['neighborhood'], 'Baixa Grande')

    def test_should_be_able_to_list_services_filtered_by_status(self):
        url = reverse('job-services', kwargs={'job_id': self.job.id})
        url_with_query = f"{url}?status=accepted&date=2024-10-10"

        response = self.client.get(
            url_with_query,
            format='json',
        )

        json_response = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['date'], '2024-10-10')
        self.assertEqual(json_response[0]['neighborhood'], 'Prado')
