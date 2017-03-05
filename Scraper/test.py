import webbrowser
import lxml
from lxml import html
import xml
import requests



url = 'http://www.argos.co.uk/static/Browse/ID72/33015263/c_1/1|category_root|Home+and+garden|33005908/c_2/2|33005908|Living+room+furniture|33008988/c_3/3|cat_33008988|Armchairs+and+chairs|33015263.htm'
url = 'http://www.argos.co.uk/product/3776056'
url = 'http://www.argos.co.uk/product/3802391'


def fetch_furniture_details(url):
    '''fetching furniture details'''
    page = requests.get(url)
    tree = html.fromstring(page.content)
    description = tree.xpath('//div[@class="product-description-content-text"]/ul/li/text()')
    product_name = tree.xpath('//div[@class="product-name"]/h1/span/text()')
    image_url = tree.xpath('//div[@class="media-player-colosseum"]/ul/li/a/img/@src')
    print product_name
    print description
    print image_url



fetch_furniture_details(url)
