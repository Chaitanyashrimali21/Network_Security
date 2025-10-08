from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
import sys

if __name__ == "__main__":
    try:
      trainingpipelineconfig = TrainingPipelineConfig()
      dataIngestionConfig=DataIngestionConfig(trainingpipelineconfig)
      data_ingestion=DataIngestion(dataIngestionConfig)
      logging.info("initiated data ingestion")
      dataingestionartifact=data_ingestion.initiate_data_ingestion()
      print(dataingestionartifact)
      logging.info("completed data ingestion")
      logging.info("initiated data validation")
      data_validation_config = DataValidationConfig(trainingpipelineconfig)
      data_validation = DataValidation(dataIngestionConfig,data_validation_config)
      data_validation_artifact =   data_validation.initiate_data_validation()
      print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)