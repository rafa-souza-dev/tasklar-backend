from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import User


class TestLogin(APITestCase):
    def setUp(self) -> None:
        self.email = 'juvenal@test.com'
        self.password = 'S6y6@9iP5Q&r5BQx'
        self.hashed_password = make_password(self.password)

        User.objects.create(email=self.email, password=self.hashed_password)

        url_login = reverse('token_obtain_pair')
        body_login = {
            'email': self.email,
            'password': self.password
        }
        response_login = self.client.post(
            url_login, body_login, format='json'
        )
        self.jwt_token = response_login.data['access']

        return super().setUp()

    def test_should_be_able_to_recieve_whoami_data(self):
        url = reverse('whoami')

        response = self.client.get(
            url,
            format='json',
            headers={ 'Authorization': f'Bearer {self.jwt_token}' }
        )

        json_response = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['user']['email'], self.email)

    def test_not_should_be_able_to_recieve_whoami_data_when_are_not_logged(self):
        url = reverse('whoami')

        response = self.client.get(
            url,
            format='json',
        )

        self.assertEqual(response.status_code, 401)
