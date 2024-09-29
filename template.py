import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s : %(message)s]:')

project_name = "kidneyDiseaseClassfier"

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
]

for file in list_of_files:
    file_path = Path(file)
    file_dir,file_path = os.path.split(file_path)
    print("ddd",file_dir,file_path)
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating file directory :{file_dir}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path))==0:
        with open(file,"w") as file:
            pass
            logging.info(f"creating empty file path :{file_path}")




