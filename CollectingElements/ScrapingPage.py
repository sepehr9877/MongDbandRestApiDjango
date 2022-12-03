from Products import Products
import requests
from bs4 import BeautifulSoup
class WebScraping:
    _product=Products()
    def __init__(self,category):
        self._url=None
        self.category=category
        self._product._connectToMongDb(self=self._product)
    def seturl(self,url):
        self._url=url
        self.setItemToProductDic()
    def setItemToProductDic(self):
        count=0
        soup = BeautifulSoup(self._url.content, 'lxml')

        newelement = soup.findAll('div', class_="p13n-sc-uncoverable-faceout")
        for el in newelement:
            selected_name = el.find_next('div', class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
            selected_image=el.find_next('img')['src']
            selected_star = el.find('span', {"class": 'a-icon-alt'})

            if selected_star is None:
                selected_star="No Rating"
            else:
                selected_star=selected_star.text
            selected_review = el.find_next('span', class_="a-size-small")
            selected_price_offer_element = el.findAll('div', {"class": 'a-row'})
            if len(selected_price_offer_element)==1:
                selected_price_offer_element=selected_price_offer_element[0]
            else:
                selected_price_offer_element=selected_price_offer_element[1]
            price = str(selected_price_offer_element.text)
            self._product.addToProductList(self=self._product,
                                     itemnumber=count,
                                    image=selected_image,
                                     name=selected_name.text
                                     , rate=selected_star
                                     , price=price,
                                     review=selected_review.text,
                                    category=self.category)
            count = count + 1
        self.setCollection()
    def setCollection(self):
        self._product.insertToMongoDb(self=self._product,category=self.category)


