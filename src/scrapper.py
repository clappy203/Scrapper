import pandas as pd
import pprint
from bs4 import BeautifulSoup
import requests



def get_srapped_data(keyword: str, item_number: int):
   
    """
        Scrape data based on keyword and number of rows to be scrapped
    
        Parameters:
        keyword: The keyword that needs to be searched
        item_number: number of examples to be scraped
    """
    titles = []
    prices = []
    urls = []
    images = []


    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
    page_num = round(item_number/64) 
    for i in range(1,page_num+1):
      pprint.pprint(i)
      page = f'https://www.etsy.com/ca/search?q={keyword}&page={i}&ref=pagination'   
      pages = requests.get(page, headers = headers)
      soup = BeautifulSoup(pages.content, "html.parser")

      for items in soup.find_all("div", class_="v2-listing-card__info"):
          title = items.find("h3", class_="wt-mb-xs-0")
          titles.append(title.text.strip())

      for price in soup.find_all("div", class_="n-listing-card__price"):
          price = price.find("span", class_="currency-value")
          prices.append(price.text)

      for image in soup.find_all("img"):
          images.append(image.get('src')) 

      for items in soup.find_all("a", class_="listing-link"):
          urls.append(items.get('href')) 
    
    data = {'title': titles, 'prices': prices, 'url to item': urls, 'url of image': images}
    data = pd.DataFrame(data)
    data['category'] = keyword

    return data

dt = get_srapped_data('phone', 64)
