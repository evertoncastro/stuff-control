import os
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from application.common.tests.test_mixins import TestMixins

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')


class AuthTokenTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.password = "mypass"
        self.user = self.create_user(password=self.password)
    
    def test_login_and_logout(self):
        url_login = reverse('authentication-token')
        data = {'email': self.user.email, 'password': self.password}
        response = self.client.post(url_login, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.json())
        self.assertIn("refresh", response.json())

        auth_data = response.json()
        url_logout = reverse('authentication-logout')
        data = {'refresh_token': auth_data['refresh']}
        response = self.client.post(url_logout, data, format='json', headers={
            'Authorization': f'Bearer {auth_data["access"]}'
        })
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
