from bs4 import BeautifulSoup
import  requests
from ScrapingPage import WebScraping
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
         'Referer':'https://www.amazon.ca/',
        }
urlhome='https://www.amazon.ca/gp/bestsellers/kitchen/?ie=UTF8&ref_=sv_k_1'
urlCraft='https://www.amazon.ca/Best-Sellers-Home-Sewing-Craft-Hobby/zgbs/kitchen/2224180011/ref=zg_bs_nav_kitchen_1'
urlArtwork='https://www.amazon.ca/Best-Sellers-Home-Artwork/zgbs/kitchen/2223977011/ref=zg_bs_nav_kitchen_1'
urlBath='https://www.amazon.ca/Best-Sellers-Home-Bath-Products/zgbs/kitchen/2223985011/ref=zg_bs_nav_kitchen_1'
urlBedding='https://www.amazon.ca/Best-Sellers-Home-Bedding/zgbs/kitchen/2223997011/ref=zg_bs_nav_kitchen_1'
urlFreshFlower='https://www.amazon.ca/Best-Sellers-Home-Fresh-Flowers-Indoor-Plants/zgbs/kitchen/2224015011/ref=zg_bs_nav_kitchen_1'
urlFurniture='https://www.amazon.ca/Best-Sellers-Home-Furniture/zgbs/kitchen/2224017011/ref=zg_bs_nav_kitchen_1'
urlHeating='https://www.amazon.ca/Best-Sellers-Home-Heating-Cooling-Air-Quality/zgbs/kitchen/6646962011/ref=zg_bs_nav_kitchen_1'
urlHomeDecor='https://www.amazon.ca/Best-Sellers-Home-Home-Dcor/zgbs/kitchen/2224027011/ref=zg_bs_nav_kitchen_1'
urlHomeTextile='https://www.amazon.ca/Best-Sellers-Home-Home-Textiles/zgbs/kitchen/13848667011/ref=zg_bs_nav_kitchen_1'
urlKitchenDinning='https://www.amazon.ca/Best-Sellers-Home-Kitchen-Dining/zgbs/kitchen/2224068011/ref=zg_bs_nav_kitchen_1'
def RequestToPage(url,categoryname):
    url_request=requests.get(url=url,headers=headers)
    AddToDB(url=url_request,category=categoryname)
def AddToDB(url,category):
    Webone = WebScraping(category=category)
    Webone.seturl(url=url)
if __name__=='__main__':
    RequestToPage(url=urlhome,categoryname="home")
    RequestToPage(url=urlCraft,categoryname='Craft')
    RequestToPage(url=urlArtwork,categoryname='ArtWork')
    RequestToPage(url=urlBath,categoryname='Bath')
    RequestToPage(url=urlBedding,categoryname='Bedding')
    RequestToPage(url=urlFreshFlower,categoryname='FreshFlower')
    RequestToPage(url=urlFurniture,categoryname='Furniture')
    RequestToPage(url=urlHeating,categoryname='urlHeating')
    RequestToPage(url=urlHomeTextile,categoryname='HomeTextile')
    RequestToPage(url=urlHomeDecor,categoryname='HomeDecor')
    RequestToPage(url=urlKitchenDinning,categoryname='KitchenDinning')




