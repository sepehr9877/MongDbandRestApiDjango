from pymongo import MongoClient
class Products:
    _ProductList=[]
    _productItem={}
    _ProdcutCollection=None
    _ProductDb=None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance=super(Products,cls).__new__(cls)
        return cls
    def __init__(self):
        self._productItem={}
        self._ProductDb=None
        self._ProductCollection=None
        self._ProductList=[]
    def _connectToMongDb(self):
        print("Connect To MongoDb")
        password='sepehr12345'
        client=MongoClient(f'mongodb+srv://sepehr:{password}@sepehr.ypt1dzn.mongodb.net/?retryWrites=true&w=majority')
        self._ProductDb=client["Amazon"]
    def setCollectionName(self,CollectionName):
        print("Set Collection Name")
        self._ProductCollection=self._ProductDb[f'{CollectionName}']
    def insertToMongoDb(self,category):
        for item in self._ProductList:
            print(item)
        self.setCollectionName(self=self,CollectionName=category)
        self._ProductCollection.insert_many(self._ProductList)
        self._ProductList=[]
        self._ProductCollection=None
    def addToProductList(self,itemnumber,name,price,rate,review,category):
        print("AddTolist")
        self._productItem['itemnumber']=itemnumber
        self._productItem['name']=name
        self._productItem['price']=price
        self._productItem['review']=review
        self._productItem['rate']=rate
        self._productItem['category']=category
        self._ProductList.append(self._productItem)
        print(self._productItem)
        self._productItem={}
    def getAllProducts(self):
        return self._ProductList

