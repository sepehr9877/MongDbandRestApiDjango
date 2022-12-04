from rest_framework import serializers
from AmazonProducts.models import Products,Category
class ProdcutsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['Title','Image','Price','Reviews','Rate','Categories']
class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','Title']
