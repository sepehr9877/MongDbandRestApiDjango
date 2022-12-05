from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
# Create your views here.
from AmazonProducts.API.serializers import ProdcutsSerializer,CategorySerialzier
from AmazonProducts.models import Products,Category
class ProductsView(ListAPIView,
                   ListModelMixin,
                   RetrieveModelMixin
                   ):
    permission_classes = []
    serializer_class = ProdcutsSerializer
    def get_queryset(self):
        queryset=Products.objects.all()[:10]
        return queryset
    def get(self, request, *args, **kwargs):
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



