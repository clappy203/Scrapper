from src.scrapper import get_scraped_data
from database.database import insert_to_database, join_and_export
import pandas as pd 
from src.category import categories


def Main():
    for keyword in categories:
        item_number = 3000
        scraped_df = get_scraped_data(keyword, item_number)
        insert_to_database(scraped_df, 'etsy_products')
        print('data scrapped successfully')
        join_and_export() 
       
Main()