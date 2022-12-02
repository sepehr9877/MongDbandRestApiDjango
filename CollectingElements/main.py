from bs4 import BeautifulSoup
import  requests
from Products import Products
product=Products()
page=[1]
count=0
r = requests.get("https://www.amazon.ca/Best-Sellers-Home/zgbs/kitchen/")
soup = BeautifulSoup(r.content, 'html.parser')
newelement = soup.findAll('div', class_="p13n-sc-uncoverable-faceout")
for el in newelement:
    selected_name=el.find_next('div',class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    selected_star=el.find('span', {"class":'a-icon-alt'})
    selected_review=el.find_next('span',class_="a-size-small")
    selected_price_offer_element=el.findAll('div', {"class":'a-row'})[1]
    offer_price=str(selected_price_offer_element.text)
    print(offer_price)
    selected_offer_price=offer_price.split("from")
    selected_offer=selected_offer_price[0]
    selected_price=selected_offer_price[1]
    product.addToProductList(itemnumber=count,
                            name=selected_name.text
                             ,rate=selected_star.text
                             ,price=selected_price,
                             offers=selected_offer,
                             review=selected_review.text)
    count=count+1
items=product.getAllProducts()
product.insertToMongoDb()
