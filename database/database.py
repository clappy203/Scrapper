import pandas as pd
from sqlalchemy.engine import result
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, engine
import config
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
db_param = config["postgresql"]
user = db_param["user"]
password = db_param["password"]
host = db_param["host"]
port = int(db_param["port"])
database = db_param["database"]


def connect_engine():
    """
    This function create a database engine for connecting to database 
    """
    try:
        db_host = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(db_host, echo= False)
        db = scoped_session(sessionmaker(bind=engine))
        return db
    except:
        print("Error connecting to database")


def insert_to_database(df: pd.DataFrame, file_title: str) -> None:
    """
    This function saves a dataframe to the database
    Args:
        df (str): the table to be stored in the database
        file_title (str): title of the output file
    Returns:
        None   
    """
    db_host = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    db = connect_engine()
    engine = create_engine(db_host, echo= False)
    df.to_sql(f'{file_title}', engine, if_exists= "append", index= False)
    db.commit()
  

def create_table():

    """ 
    This function creates the category table 
    """
    create_engine()
    engine.execute('CREATE TABLE IF NOT EXISTS categories (id serial PRIMARY KEY, category VARCHAR)')
    print('created categories')


def insert_into_table():
    """ 
    This function inserts unique categories into the database 
    """
    create_engine()
    engine.execute("INSERT INTO categories (category) VALUES ('phone')")
    engine.execute("INSERT INTO categories (category) VALUES ('shirt')")
    engine.execute("INSERT INTO categories (category) VALUES ('watch')")
    print('data inserted successfully')


def join_and_export():
    """
    Execute query, fetch all the records and export it to csv file.
    Returns csv file containing all the records in the database
    """

    db_host = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    db = connect_engine()
    engine = create_engine(db_host, echo= False)
  
    query = engine.execute("""select categories.category, etsy_products.title, etsy_products.prices, 
                            etsy_products.url_to_item, etsy_products.url_of_image 
                           from etsy_products LEFT JOIN categories on etsy_products.category = categories.category""")
    print('table created successfully')
    df = pd.DataFrame(query.fetchall(),columns=query.keys())
    df.to_csv("C:\\Users\\hp\\Documents\\Scrapper\\results_csv\\joned_data_etsy.csv", index= False)
 
