import os
import pandas as pd
import numpy as np
# import mysql.connector
# import pymongo
import sys
from src.logger import logging
from src.exception import CustomException

# Ingesting the Dataset from the MySQL server:
def read_from_MySQL(host,user,password,db_name,table_name):
    try:
        conn=mysql.connector.connect(host=host,user=user,password=password,db=db_name,)
        query=f'select * from {table_name}'
        df=pd.read_sql(query,conn)
        conn.disconnect()
        conn.close()
        return df
        logging.info('Dataset read successfully from MySQL')

    except Exception as e:
        logging.info('There is a problem in loading dataset from MySQL')
        raise CustomException(e,sys)

# Ingesting the dataset from MongoDB:
def read_from_Mongo(uri,db_name,conn_name,query):
    logging.info('MongoDb connection is establishing')
    try:
        mongo_client=pymongo.MongoClient(uri)
        database=mongo_client[db_name]
        collection=database[conn_name]
        df=pd.DataFrame(i for i in connection.find({query}))
        return df
        logging.info('Dataset read successfully from MongoDB')
    except Exception as e:
        logging.info('There is a problem in loading dataset from MongoDB')
        raise CustomException(e,sys)


# Function for extra space removal (Stripping of the text):
def strip_text(df):
    for i in df.columns:
        if df[i].dtype=='object':
            df[i]=df[i].map(str.strip)
        else:
            pass
    return df

# Function for saving the objects:
# def save_objects(file_path, obj):