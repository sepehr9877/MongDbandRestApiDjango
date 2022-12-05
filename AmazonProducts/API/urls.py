from django.urls import path
from AmazonProducts.API.views import ProductsView,CategoryView,GetProductDetail,ProductDetailByCategory
urlpatterns=[
    path('ProductsList',ProductsView.as_view()),
    path('CategoryList/<int:id>',CategoryView.as_view()),
    path('ProductDetail/<int:id>',GetProductDetail.as_view()),
    path('ProductByCategory/<int:id>',ProductDetailByCategory.as_view())
]