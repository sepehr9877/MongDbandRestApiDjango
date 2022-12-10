from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from requests import request
class TestProductApI(APITestCase):
    def setUp(self):
        self.url="http://127.0.0.1:8000/ProductsList"
    def test_send_get_request(self):
        username="ali"
        password="ali12345"
        send_request=request(method="get",url=self.url,auth=(username,password))
        print(send_request.text)
# Create your tests here.
