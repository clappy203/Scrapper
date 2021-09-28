import pandas as pd
import pprint
from bs4 import BeautifulSoup
import requests
from typing import Union


def get_scraped_data(keyword: str, item_number: int):
   
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
    pages = int(item_number/64 if item_number % 12 == 0 else (item_number/12)+1)
    
    
    for i in range(pages):

    #   pprint.pprint(i)
      page_link = f'https://www.etsy.com/ca/search?q={keyword}&page={i}&ref=pagination'   
      page = requests.get(page_link, headers = headers)
      soup = BeautifulSoup(page.content, "html.parser")

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

    
    data = {'category': keyword, 'title': titles, 'prices': prices, 'url_to_item': urls, 'url_of_image': images}
    data = pd.DataFrame(data)


    return data

def create_csv(data: pd.DataFrame, file_title: str) -> None:
    """
    This function converts a dataframe to a csv
    Args:
        data (pd.DataFrame): the dataframe to be converted to csv
    Returns:
        None   
    """
    data.to_csv(f'{file_title}.csv', index= False)
