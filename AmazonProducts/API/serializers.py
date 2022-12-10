from rest_framework import serializers
from AmazonProducts.models import Products,Category
from rest_framework.serializers import CharField
class ProdcutsSerializer(serializers.ModelSerializer):
    token=CharField(read_only=True)
    class Meta:
        model=Products
        fields=['id','Title','Image','Price','Reviews','Rate','Categories','token']

class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','Title']
