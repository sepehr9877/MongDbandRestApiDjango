import os.path

from django.contrib.auth.models import User

from Account.models import Account
from django.test import TestCase
from rest_framework.test import APITestCase
from requests import request
class TestAccountApi(TestCase):
    def setUp(self):
        self.url='http://127.0.0.1:8000/LoginPage/'
        self.register="http://127.0.0.1:8000/CreateAccount/"
        self.updateurl="http://127.0.0.1:8000/UpdateAccount/56"
        created_user=User.objects.create(username="sam",last_name="sam",email="sam@yahoo.com")
        Account.objects.create(UserAccount_id=created_user.id,ImageFile=None)
    def test_login_api(self):
        username="ali"
        password="ali12345"
        data={"username":username,
              "password":password}
        send_request=request(method='post',url=self.url,data=data)
    def test_register_api(self):
        data={}
        data['ImageFile']=None
        data["firstname"] = "sara"
        data['lastname'] = "sara"
        data["password"] = "sara12345"
        data["repassword"] = "sara1234"
        data["email"] = "sara@yahoo.com"
        send_request=request(method='post',url=self.register,data=data)
        print(send_request.text)



# Create your tests here.
