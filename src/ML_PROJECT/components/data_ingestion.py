import os
import pandas as pd
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import CustomeException
import sys
from dataclasses import dataclass
from src.ML_PROJECT.utils import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    row_data_path: str = os.path.join("artifacts", "row.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()

    def read_data(self):
        try:
            logger.logging.info("Start Reading Data From SQL")
            df = read_sql_data()
            os.makedirs(
                os.path.dirname(self.data_ingestion.row_data_path), exist_ok=True
            )
            df.to_csv(self.data_ingestion.row_data_path, index=False, header=True)
            logger.logging.info("Raw.csv FIle Created Successfully")

            train_data_set, test_data_set = train_test_split(
                df, test_size=0.20, random_state=42
            )
            train_data_set.to_csv(
                self.data_ingestion.train_data_path, index=False, header=True
            )
            logger.logging.info("Train.csv FIle Created Successfully")

            test_data_set.to_csv(
                self.data_ingestion.test_data_path, index=False, header=True
            )
            logger.logging.info("Test.csv FIle Created Successfully")

            return (
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path,
            )

        except Exception as e:
            raise CustomeException(e, sys)
