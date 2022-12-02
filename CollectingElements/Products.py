from pymongo import MongoClient
class Products:
    _ProductList=[]
    _productItem={}
    _ProdcutCollection=None
    _ProductDb=None
    _ProductCollection=None
    def __new__(cls):
        if not hasattr(cls,'_instnace'):
            cls._instance=super(Products,cls).__new__(cls)
        return cls._instance
    def _connectToMongDb(self):
        password='sepehr12345'
        client=MongoClient(f'mongodb+srv://sepehr:{password}@sepehr.ypt1dzn.mongodb.net/?retryWrites=true&w=majority')
        self._ProductDb=client["Amazon"]
        self._ProductCollection=self._ProductDb["AmazonProducts"]
    def insertToMongoDb(self):
        for item in self._ProductList:
            print(item)
        self._connectToMongDb()
        self._ProductCollection.insert_many(self._ProductList)
    def addToProductList(self,itemnumber,name,rate,price,offers,review):
        self._productItem['itemnumber']=itemnumber
        self._productItem['name']=name
        self._productItem['price']=price
        self._productItem['offers']=offers
        self._productItem['review']=review
        self._productItem['rate']=rate
        print(self._productItem)
        self._ProductList.append(self._productItem)
        self._productItem={}
    def getAllProducts(self):
        return self._ProductList

