from Winequality import logger
from Winequality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Winequality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Winequality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Winequality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from Winequality.pipeline.stage_01_data_ingestion import *

STAGE_NAME = "Data Ingestion Pipeline"
if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} data ingestion started")
        obj = DataIngestionTrainingPipeline()
        obj.main()

        logger.info(f"Stage {STAGE_NAME} data ingestion completed")
    
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data Validation Pipeline"
if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME}  started")
        obj = DataValidationTrainingPipeline()
        obj.main()

        logger.info(f"Stage {STAGE_NAME} completed")
    
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data Transformation Pipeline"
if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME}  started")
        obj = DataTransformationTrainingPipeline()
        obj.main()

        logger.info(f"Stage {STAGE_NAME} completed")
    
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Training Pipeline"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e