from sqlalchemy import create_engine
import config
from src import scrapper
from scrapper import get_srapped_data

database=config.database,
user=config.user,
password=config.password,
host=config.hostname,
port=config.port

categories = [
    "phone",
    "shoe",
    "bag",
    "watch"
]

for category in categories:
        item_number = 3000
        scraped_df = get_srapped_data(category, item_number)