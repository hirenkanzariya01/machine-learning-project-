from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import CustomeException
import sys
from src.ML_PROJECT.components.data_ingestion import DataIngestion

try:
    dataIngestionObj = DataIngestion()
    dataIngestionObj.read_data()

except Exception as e:
    logger.logging.info(CustomeException(e, sys))
    raise CustomeException(e, sys)
