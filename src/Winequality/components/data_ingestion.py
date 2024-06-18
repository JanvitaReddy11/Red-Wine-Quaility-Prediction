import os
import urllib.request as request
import zipfile
from src.Winequality import logger
from src.Winequality.utils.common import get_size
from Winequality.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    ## Download file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file)
            logger.info(f"{filename} download")
        else:
            logger.info(f"File aready exists:{get_size(Path(self.config.local_data_file))}")


    ## Unzip:

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as f:
            f.extractall(unzip_path)




            
