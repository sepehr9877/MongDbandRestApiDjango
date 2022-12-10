import os.path

from django.test import TestCase
from rest_framework.test import APITestCase
from requests import request
class TestAccountApi(TestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000/LoginPage/'
        self.register="http://127.0.0.1:8000/CreateAccount/"
    def test_login_api(self):
        username="ali"
        password="ali12345"
        data={"username":username,
              "password":password}
        send_request=request(method='post',url=self.url,data=data)
    def test_register_api(self):
        data={}
        with open('../image/Amazon-Logo-Black.jpg') as ImageFile:
            data["firstname"] = "sara"
            data['lastname'] = "sara"
            data["password"] = "sara12345"
            data["repassword"] = "sara1234"
            data["email"] = "sara@yahoo.com"
            data['ImageFile']=ImageFile
            send_request=request(method='post',url=self.register,data=data)
            print(send_request.text)


# Create your tests here.
