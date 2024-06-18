from Winequality import logger
#from Winequality.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Winequality.pipeline.stage_01_data_ingestion import *

STAGE_NAME = "Data Ingestion Pipeline"
if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} data ingestion started")
        obj = DataIngestionPipeline()
        obj.main()

        logger.info(f"Stage {STAGE_NAME} data ingestion completed")
    
    except Exception as e:
        logger.exception(e)
        raise e