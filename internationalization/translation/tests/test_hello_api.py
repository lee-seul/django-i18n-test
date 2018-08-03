# coding: utf-8

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestHelloAPI(APITestCase):
    
    def test_hello_api(self):
        url = reverse('translation:hello')

        headers = {
            'HTTP_ACCEPT_LANGUAGE': 'kr'
        }

        # 한국어 테스트
        response = self.client.get(url, headers={}, **headers)
        data = response.json()

        self.assertEqual(data['result'], '테스트')

        # english 
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(data['result'], 'Test')