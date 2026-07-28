from src.ML_PROJECT.exception import CustomeException
from src.ML_PROJECT import logger
import sys

try:
    paint("this is error ")
except Exception as e:
    logger.logging.info(CustomeException(e, sys))
    raise CustomeException(e, sys)
