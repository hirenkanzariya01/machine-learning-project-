import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name = "ML_PROJECT"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "main.py",
]

for fp in list_of_files:
    file_path = Path(fp)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if not os.path.exists(file_path) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
