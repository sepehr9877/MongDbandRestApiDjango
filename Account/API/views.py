from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin,CreateModelMixin
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializer import AccountSerializer
from Account.models import Account
class CreateAccountPage(ListAPIView,CreateModelMixin):
    permission_classes = []
    serializer_class = AccountSerializer
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):
        serializer_user=AccountSerializer()
        serializer_user.validate_email(value=self.request.data['email'])
        serializer_user.validate_username(value=self.request.data['firstname'])
        serializer_user=AccountSerializer(data=self.request.data)
        return self.create(request,*args,**kwargs)


