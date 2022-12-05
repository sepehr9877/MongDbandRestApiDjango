from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin,CreateModelMixin
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializer import AccountSerializer
class CreateAccountPage(ListAPIView,CreateModelMixin):
    permission_classes = []
    serializer_class = AccountSerializer
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):
        serializer_user=AccountSerializer(data=self.request.data or self.request.FILES)
        serializer_user.validate_Email(value=self.request.data['Email'])
        serializer_user.validate_Firstname(value=self.request.data['FirstName'])
        if serializer_user.is_valid():
            serializer_user.create(validated_data=AccountSerializer(data=self.request.data).validated_data)
        return self.create(request,*args,**kwargs)

