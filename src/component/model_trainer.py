import os
import sys
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report, f1_score
from src.exception import CustomException
from src.logger import logging
from src.utils import save_objects
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Initiating model training')
            logging.info('Performing Train-Test-Split')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            model= LogisticRegression(penalty='l2',C=0.1,max_iter=100)
            model.fit(X_train,y_train)

            y_pred=model.predict(X_test)
            test_score=accuracy_score(y_test,y_pred)
            report = classification_report(y_test,y_pred)

            print(f"Model name: Logistic regression, Accuracy score: {test_score}")
            logging.info(f"Model name: Logistic regression, Accuracy score: {test_score}")

            print("="*40)
            print(f"Classification report: \n {report}")

            logging.info(f'Classification report: \n {report}')

            save_objects(
                self.model_trainer_config.trained_model_file_path,
                obj=model
            )
        except Exception as e:
            logging.info('Error occured at model training stage')
            raise CustomException(e,sys)