import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "Backpack Prediction Challenge"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_Transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/visualization/__init__.py",
    f"src/{project_name}/visualization/plot.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    f"src/notebooks/__init__.py",
    f"src/notebooks/data/__init__.py",
    f"src/notebooks/Eda_trainer.ipynb",
    f"src/notebooks/Model_Trainer.ipynb",
    "requirements.txt",
    "Dokerfile",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    

    
    if filedir != "":
        os.makedirs (filedir, exist_ok=True)
        logging.info(f"Directory created for {filedir} and file created for {filename}")
    
    
    
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        filepath.touch()
        logging.info(f"File created for {filepath}")
    else:
        logging.info(f"File already exists for {filepath}")
    
        

    


    
    