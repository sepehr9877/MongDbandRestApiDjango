from django.urls import path
from .views import ProductsView,CategoryView
urlpatterns=[
    path('ProductsList',ProductsView.as_view()),
    path('CategoryList/<int:id>',CategoryView.as_view())
]