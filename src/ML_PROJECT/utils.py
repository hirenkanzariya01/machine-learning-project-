import sys
import os
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import CustomeException
from dotenv import load_dotenv
import pymysql
import pandas as pd

load_dotenv()

HOST = os.getenv("host")
USER = os.getenv("user")
PASSWORD = os.getenv("password")
DB = os.getenv("db")


def read_sql_data():
    logger.logging.info("Start Reading Data From MySQL")
    try:
        connect_sql = pymysql.connect(user=USER, host=HOST, password=PASSWORD, db=DB)
        logger.logging.info("My Sql Connect Successfully")
        df = pd.read_sql_query("SELECT * from medical_insurance", connect_sql)
        logger.logging.info(f"Sample Data {df.head}")
        return df

    except Exception as e:
        logger.logging.info(CustomeException(e, sys))
        raise CustomeException(e, sys)
