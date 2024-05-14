import os
import pandas as pd
import numpy as np
import pickle
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
        df=pd.DataFrame(i for i in collection.find({query}))
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
def save_objects(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info('Error occured in saving object')
        raise CustomException(e,sys)
    

#Function for loading objects
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Error occured in loading object')
        raise CustomException(e,sys)
    
# Replacing the hyphen sigh with the underscore in the column names 
def underscore(df):
    df.columns = df.columns.map(lambda x:x.replace('-','_'))
    return df