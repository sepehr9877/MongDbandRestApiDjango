from django.urls import path
from .views import LogingPage,Register
urlpatterns=[
    path('Login_Page',LogingPage),
    path('Register_Page',Register),
]