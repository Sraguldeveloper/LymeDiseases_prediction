import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataConfig():
    train_data_path = os.path.join('Artifacts','train.csv')
    test_data_path = os.path.join('Artifacts','test.csv')
    raw_data_path = os.path.join('Artifacts','data.csv')
class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataConfig()
    def intialteIngestion(self):
        logging.info("Initialsed the data ingestion method")
        try:
            df = pd.read_csv('C:/Users/sragu/OneDrive/Desktop/machinelearning/Notebook/LymeDisease_9211_county.csv')
            logging.info('Reading datasets')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)
            logging.info("Data is created")
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=50)
            logging.info("Data got splitted to train and test set")
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    dataInject = DataIngestion()
    dataInject.intialteIngestion()