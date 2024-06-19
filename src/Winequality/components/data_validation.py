
from src.Winequality import logger
from src.Winequality.utils.common import get_size
from Winequality.entity.config_entity import DataValidationConfig
from pathlib import Path
import os
import pandas as pd # type: ignore

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file,'w') as f:
                        f.write(f'Validation status:{validation_status}')

                else:
                    validation_status = True
                    with open(self.config.status_file,'w') as f:
                        f.write(f'Validation status:{validation_status}')

            return validation_status
        
        except Exception as e:
            raise e