import os
import sys
import pandas as pd
from src.logger import logger
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
        os.makedirs('artifacts', exist_ok=True)
        logger.info("Artifacts directory created or verified")

    def initiate_data_ingestion(self):
        logger.info('Starting data ingestion process')
        try:
            # Use relative path from project root
            data_path = r'C:\Users\divak\OneDrive\Desktop\ml projects\notebook\data\Stud.csv'
            logger.info(f'Reading dataset from: {data_path}')
            
            df = pd.read_csv(data_path)
            logger.info(f'Dataset read successfully with shape: {df.shape}')

            # Save raw data
            df.to_csv(self.config.raw_data_path, index=False)
            logger.info(f'Raw data saved to: {self.config.raw_data_path}')

            # Split data
            logger.info('Splitting data into train and test sets')
            train_data, test_data = train_test_split(
                df, 
                test_size=0.2, 
                random_state=42
            )
            
            # Save train and test data
            train_data.to_csv(self.config.train_data_path, index=False)
            test_data.to_csv(self.config.test_data_path, index=False)
            logger.info(f'Train data saved to: {self.config.train_data_path}')
            logger.info(f'Test data saved to: {self.config.test_data_path}')

            logger.info('Data ingestion completed successfully')
            
            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            logger.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)

if __name__ == '__main__':
    try:
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        logger.info(f"Data ingestion successful. Train: {train_path}, Test: {test_path}")
    except Exception as e:
        logger.error(f"Data ingestion failed: {str(e)}")
        raise