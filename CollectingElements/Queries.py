from pprint import pprint
import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='MongDbandRestApiDjango.settings'
django.setup()
from AmazonProducts.models import Products,Category
from pymongo import MongoClient
password='sepehr12345'
client=MongoClient(f'mongodb+srv://sepehr:{password}@sepehr.ypt1dzn.mongodb.net/?retryWrites=true&w=majority')
AmazonDb=client['Amazon']
HeatCollection=AmazonDb['urlHeating']
CursorObject_ListCategories=[]
CategoryList=[]
CollectionList=[]
ProductList_CursorObject=[]
ProductList=[]
def updatecateroy():
    HeatCollection.update_many({},{"$set":{"category":"Heating"}})
def Collect_collections():
    collectionsName=AmazonDb.list_collection_names()
    for collection in collectionsName:
        CollectionList.append(collection)
def getAllCategories():
    for collection in CollectionList:
        selected_collection=AmazonDb[collection]
        selected_item=selected_collection.aggregate(
            [
                {"$group":{
                    "_id":{"category":"$category"},
                    "category":{"$first":"$category"}
                }
                }
            ]
        )

        CursorObject_ListCategories.append(selected_item)
    List_Categories=set(CursorObject_ListCategories)
    for items in List_Categories:
        for item in items:
            CategoryList.append(item)
def AddToCategoryModel():
    for item in CategoryList:
        for key in item:
            if key=='category':
                Category.objects.update_or_create(Title=item[key])
def AddToProductList():
    for collection in CollectionList:
        selected_Collection=AmazonDb[collection]
        selected_items=selected_Collection.aggregate(
            [
                {"$project":{"name":1,"price":1,"review":1,"rate":1,'category':1,"imageUrl":1}},
                {"$group":{
                    "_id":{"name":"$name"},
                    "Title":{"$first":"$name"},
                    "Image":{"$first":"$imageUrl"},
                    "Price":{"$first":"$price"},
                    "Review":{"$first":"$review"},
                    "Rate":{"$first":"$rate"},
                    'Category':{"$first":"$category"}
                }
                 }
            ]
        )
        ProductList_CursorObject.append(selected_items)
    for items in ProductList_CursorObject:
        for item in items:
            ProductList.append(item)

def AddToProductModel():
    for item in ProductList:
        Products.objects.update_or_create(
            Title=item['Title'],
            Image=item['Image'],
            Rate=item['Rate'],
            Price=item['Price'],
            Reviews=item['Review'],
            Categories_id=Category.objects.get_category_id(name=item['Category'])

        )
if __name__=="__main__":
    Collect_collections()
    getAllCategories()
    AddToCategoryModel()
    AddToProductList()
    AddToProductModel()
