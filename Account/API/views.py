from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView
from .permissions import AccountPermission
# Create your views here.
from .serializer import AccountSerializer,LoginSerializer,UpdatingUserSerializer
from Account.models import Account
from django.contrib.sites.models import Site
class CreateAccountPage(ListAPIView,CreateModelMixin):
    permission_classes = []
    serializer_class = AccountSerializer
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):
        serializer=AccountSerializer(data=self.request.data)
        print(self.request.data)
        serializer.context['url']=self.request
        if serializer.is_valid():
            print("valid")
            user=serializer.create(validated_data=serializer.validated_data)
            return Response({"User Created":user},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({"Errors":serializer.errors})
class UpdateAccountPage(ListAPIView,
                        UpdateModelMixin,
                        RetrieveModelMixin,
                        DestroyModelMixin):
    serializer_class = UpdatingUserSerializer
    # permission_classes = [AccountPermission]
    lookup_field = 'id'
    def get_queryset(self,*args,**kwargs):
        id=self.kwargs['id']
        queyset=Account.objects.filter(id=id)
        return queyset
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        serializer=UpdatingUserSerializer(data=self.request.data)
        serializer.context['request'] = self.request
        if serializer.is_valid():
            kwargs['partial'] = True
            return self.update(request,*args,**kwargs)
        else:
            return Response({"Not Valid":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)
class LoginUser(ListAPIView):
    serializer_class = LoginSerializer
    permission_classes = []
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):

        serializer=LoginSerializer(data=self.request.data)
        username,password=serializer.valdate_user()
        print(username,password)
        user_auth=authenticate(self.request,username=username,password=password)
        if user_auth:
            login(request=self.request,user=user_auth)
            return Response({
                "User Login":"You Are Authenticated",
                "Authenticate":True
            },status=status.HTTP_200_OK)
        return Response(
            {"User Doesnt Exist": "Please Try Again",
             "Authenticate":False}, status=status.HTTP_200_OK
        )



