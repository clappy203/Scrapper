# Web Scraper

This is a web scrapping project that scrapes from an ecommerce website (Etsy) and saves to database. This website sells different varieties of items, we will be accessing individual items by keyword and scrape the:

    - title

    - price

    - url_to_item
    
    - url_of_image

The database, etsy-project2 - where the data is pushed to- is hosted on Heroku.

****The project contains the:****

    scraper.py - For scraping data

    database.py - For inserting data to db

****Installation****

    pip install bs4

    pip install request

    pip install Sqlalchemy

****Usage****

    The datascrapper.py takes in 2 parameters, the keyword/item you want to scrape and the number of rows you want to scrape

    The maximum number of items on an etsy page is 64, hence, you must scrape 64 and above.

    The database.py file requires a write access to db

****Sample code****

    get_scraped_data('shirt',3000)

****Development****

    The project is currently completed but open to modifications
