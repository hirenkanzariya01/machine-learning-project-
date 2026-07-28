import os
import pandas as pd
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import CustomeException
import sys
from dataclasses import dataclass
from src.ML_PROJECT.utils import read_sql_data

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
            print("data path from another class", self.data_ingestion.test_data_path)

        except Exception as e:
            raise CustomeException(e, sys)

