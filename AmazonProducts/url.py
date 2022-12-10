from django.urls import path
from .views import Productspage
urlpatterns=[
    path('Products',Productspage)
]