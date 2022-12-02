class Products:
    _ProductList=[]
    _productItem={}
    _ProdcutCollection=None
    def __new__(cls):
        if not hasattr(cls,'_instnace'):
            cls._instance=super(Products,cls).__new__(cls)
        return cls._instance
    def connectToMongDb(self):
        pass
    def addToProductList(self,name,rate,price,offers,review):
        self._productItem['name']=name
        self._productItem['price']=price
        self._productItem['offers']=offers
        self._productItem['review']=review
        self._ProductList.append(self._productItem)

