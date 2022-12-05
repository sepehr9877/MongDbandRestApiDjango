from django.urls import path
from Account.API.views import CreateAccountPage
urlpatterns=[
    path('CreateAccount/',CreateAccountPage.as_view())
]