from django.urls import path
from Account.API.views import CreateAccountPage,UpdateAccountPage,LoginUser
urlpatterns=[
    path('CreateAccount/',CreateAccountPage.as_view()),
    path('UpdateAccount/<int:id>',UpdateAccountPage.as_view()),
    path('LoginPage/',LoginUser.as_view())
]