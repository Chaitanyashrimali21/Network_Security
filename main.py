from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
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
    except Exception as e:
        raise NetworkSecurityException(e, sys)