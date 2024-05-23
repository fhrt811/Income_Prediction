# Importing necessary libraries
import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from src.utils import strip_text, underscore
from dataclasses import dataclass
from src.component.data_transformation import DataTransformation

# Defining class DataIngestionConfig
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): # Method for reading the csv file, splitting into train.csv and test.csv
        logging.info('Data ingestion started')
        try:
            df=pd.read_csv('Notebooks/Data/AdultCensusIncome.csv') # Reading the csv file as pandas DataFrame 
            logging.info('Dataset read as pandas dataframe')
            df.drop_duplicates(keep='first',inplace=True)
            logging.info('Dropping the duplicate records from the dataset')
            df = strip_text(df) # Removing the extra space from the records
            df = underscore(df) # Removing the hyphen and applying under score in the column names
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            logging.info('Train-Test split')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Data ingestion has been completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occured at data ingestion stage')
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    # # Running data_transformation
    # Data_transformation=DataTransformation()
    # train_arr,test_arr,_=Data_transformation.initiate_data_transformation(train_data,test_data)