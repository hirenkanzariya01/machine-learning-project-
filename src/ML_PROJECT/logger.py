from datetime import datetime
import os
import logging

FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%S_%M_%H')}.log"
FOLDER_NAME = os.path.join(os.getcwd(), "logs")
os.makedirs(FOLDER_NAME, exist_ok=True)

LOG_FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)-8s | %(name)s | Line:%(lineno)d | %(funcName)s() | %(message)s",
    level=logging.INFO,
)
