from bs4 import BeautifulSoup
import  requests
from Products import Products
r=requests.get("https://www.amazon.ca/Best-Sellers-Home/zgbs/kitchen/ref=zg_bs_pg_2?_encoding=UTF8&pg=1")
print(r)
soup=BeautifulSoup(r.content,'html.parser')
newelement=soup.findAll('div',class_="p13n-sc-uncoverable-faceout")
product=Products()
for el in newelement:
    selected_name=el.find_next('div',class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    selected_star=el.find('span', {"class":'a-icon-alt'})
    selected_review=el.find_next('span',class_="a-size-small")
    selected_price=el.findAll('div', {"class":'a-row'})[1]
    print(selected_price.text)

