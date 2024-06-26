import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            return pred
        
        except Exception as e:
            logging.info('Exception occured in prediction')
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 age:float,
                 education_num:float,
                 capital_gain:float,
                 capital_loss:float,
                 hours_per_week:float,
                 workclass:str,
                 education:str,
                 marital_status:str,
                 occupation:str,
                 relationship:str,
                 race:str,
                 sex:str):
        
        self.age=age
        self.education_num=education_num
        self.capital_loss=capital_loss
        self.capital_gain=capital_gain
        self.capital_loss=capital_loss
        self.hours_per_week=hours_per_week
        self.workclass=workclass
        self.education=education
        self.marital_status=marital_status
        self.occupation=occupation
        self.relationship=relationship
        self.race=race
        self.sex=sex

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
                'age':[self.age],
                'education_num':[self.education_num],
                'capital_loss':[self.capital_loss],
                'capital_gain':[self.capital_gain],
                'capital_loss':[self.capital_loss],
                'hours_per_week':[self.hours_per_week],
                'workclass':[self.workclass],
                'education':[self.education],
                'marital_status':[self.marital_status],
                'occupation':[self.occupation],
                'relationship':[self.relationship],
                'race':[self.race],
                'sex':[self.sex]
            }
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe gathered')
            return df
        except Exception as e:
            logging.info('Error occured in DataFrame gathering by dictionary')
            raise CustomException(e,sys)