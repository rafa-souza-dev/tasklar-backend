from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import User
from consumer.models import Consumer
from tasker.models import Tasker


class TestRegister(APITestCase):
    def setUp(self) -> None:
        self.email = 'juvenal@test.com'
        self.password = 'S6y6@9iP5Q&r5BQx'
        self.hashed_password = make_password(self.password)

        User.objects.create(email=self.email, password=self.hashed_password)

        return super().setUp()

    def test_should_be_able_to_register_a_tasker(self):
        url = reverse('create_user')
        body = {
            'email': 'juvenal2@test.com',
            'password': self.password,
            'name': 'Rafira',
            'uf': 'PE',
            'city': 'Pesqueira',
            'phone': '(87) 98888-8888',
            'profile_type': 'T'
        }

        response = self.client.post(
            url, body, format='json'
        )

        tasker = Tasker.objects.filter(user_id=response.data['id']).first()

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['id'] != None)
        self.assertTrue(response.data['email'] != None)
        self.assertTrue(tasker != None)

    def test_should_be_able_to_register_a_consumer(self):
        url = reverse('create_user')
        body = {
            'email': 'juvenal2@test.com',
            'password': self.password,
            'name': 'Rafira',
            'uf': 'PE',
            'city': 'Pesqueira',
            'phone': '(87) 98888-8888',
            'profile_type': 'C'
        }

        response = self.client.post(
            url, body, format='json'
        )

        consumer = Consumer.objects.filter(user_id=response.data['id']).first()

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['id'] != None)
        self.assertTrue(response.data['email'] != None)
        self.assertTrue(consumer != None)

    def test_should_not_be_able_to_register_when_email_already_in_use(self):
        url = reverse('create_user')
        body = {
            'email': self.email,
            'password': self.password
        }

        response = self.client.post(
            url, body, format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(len(response.data['email']) > 0)

    def test_should_not_be_able_to_register_with_invalid_password_format(self):
        url = reverse('create_user')
        body = {
            'email': 'juvenal2@test.com',
            'password': '123456789',
            'name': 'Rafira',
            'uf': 'PE',
            'city': 'Pesqueira',
            'phone': '(87) 98888-8888',
            'profile_type': 'C'
        }

        response = self.client.post(
            url, body, format='json'
        )

        self.assertEqual(response.status_code, 422)

    def test_should_not_be_able_to_register_without_email(self):
        url = reverse('create_user')
        body = {
            'password': self.password
        }

        response = self.client.post(
            url, body, format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(len(response.data['email']) > 0)

    def test_should_not_be_able_to_register_without_password(self):
        url = reverse('create_user')
        body = {
            'email': self.email
        }

        response = self.client.post(
            url, body, format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(len(response.data['password']) > 0)

    def test_should_not_be_able_to_register_with_invalid_phone_format(self):
        url = reverse('create_user')
        body = {
            'email': 'juvenal2@test.com',
            'password': self.password,
            'name': 'Rafira',
            'uf': 'PE',
            'city': 'Pesqueira',
            'phone': '123213213',
            'profile_type': 'C'
        }

        response = self.client.post(
            url, body, format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(len(response.data['phone']) > 0)
