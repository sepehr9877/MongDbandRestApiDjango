from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from AmazonProducts.API.serializers import ProdcutsSerializer,CategorySerialzier
from AmazonProducts.models import Products,Category
from rest_framework.permissions import IsAuthenticated,AllowAny
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10

class ProductsView(ListAPIView,
                   ListModelMixin,
                   RetrieveModelMixin
                   ):
    serializer_class = ProdcutsSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset=Products.objects.all()[:1]
        return queryset
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return self.list(request,*args,**kwargs)
class ProductDetailByCategory(ListAPIView,ListModelMixin):
    permission_classes = []
    serializer_class =ProdcutsSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        queryset=Products.objects.filter(Categories_id=id).all()
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(self,*args,**kwargs)
class CategoryView(ListAPIView,ListModelMixin):
    permission_classes = []
    serializer_class =CategorySerialzier
    lookup_field = 'id'
    def get_queryset(self,*args,**kwargs):
        id=self.kwargs['id']
        queryset=Category.objects.filter(id=id).all()
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
class GetProductDetail(ListAPIView,ListModelMixin):
    permission_classes = []
    serializer_class = ProdcutsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id=self.kwargs['id']
        queryset=Products.objects.filter(id=id).all()
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)



