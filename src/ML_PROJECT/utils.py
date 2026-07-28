import sys
import os
from src.ML_PROJECT import logger
from src.ML_PROJECT.exception import CustomeException
from dotenv import load_dotenv
import pymysql

load_dotenv()

HOST = os.getenv("host")
ROOT = os.getenv("root")
PASSWORD = os.getenv("password")
DB = os.getenv("db")


def read_sql_data():
    print(" ENV DATA  :-", HOST, ROOT, PASSWORD, DB)

