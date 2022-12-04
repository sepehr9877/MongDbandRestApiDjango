from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
# Create your views here.
from .serializers import ProdcutsSerializer,CategorySerialzier
from .models import Products,Category
class ProductsView(ListAPIView,ListModelMixin):
    permission_classes = []
    serializer_class = ProdcutsSerializer
    def get_queryset(self):
        queryset=Products.objects.all()[:10]
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
class CategoryView(ListAPIView,ListModelMixin):
    permission_classes = []
    serializer_class =CategorySerialzier
    lookup_field = 'id'
    def get_queryset(self):
        
        queryset=Category.objects.get(id=id)
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

