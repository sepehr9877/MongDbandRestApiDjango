from django.urls import path
from .views import LogingPage,Register,Updating
urlpatterns=[
    path('Login_Page',LogingPage),
    path('Register_Page',Register),
    path('UpdatingProfile',Updating)
]