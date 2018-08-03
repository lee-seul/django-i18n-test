# coding: utf-8

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestHelloAPI(APITestCase):
    
    def test_hello_api(self):
        url = reverse()