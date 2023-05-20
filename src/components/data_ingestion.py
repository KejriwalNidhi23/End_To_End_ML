import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


'''
Defining a class to declare the path for multiple purposes (train_data, test_data, or any output)
Using @dataclass detractor allows us to define our set of variables in the class, otherwise we have to use init and initialize the variables
Artifact is a folder where all the files will be saved
'''
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts",'train.csv')
    test_data_path: str = os.path.join("artifacts",'test.csv')
    raw_data_path: str = os.path.join("artifacts",'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #Right now data is read from local folder, this can be changed to read from anywhere (MongoDB/MySQL/etc.)
            data = pd.read_csv(r'src\notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Create artifacts folder, if exist then ok
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train Test Split initiated')

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=1)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Ingestion of the data is completed')

            # These paths will be required to read the data for transformation
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) 
        except Exception as e:
            raise CustomException(e,sys)

'''
If you invoke your module as a script, for instance, then Python Interpreter will automatically assign the string'__main__' to the special variable __name__.
On the other hand, if your module is imported in another module then the string 'my_module' (python script name) will be assigned to __name__ .
'''
if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_path, test_path)
    
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))