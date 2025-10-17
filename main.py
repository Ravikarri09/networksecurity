from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.cinfig_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.cinfig_entity import TrainingPipelineConfig
import sys
if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the dataingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging .info("completed the dataingestion")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initiate the data validation")
        logging.info("data validation completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)