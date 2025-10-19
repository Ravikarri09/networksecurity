import sys,os
from networksecurity.logging.logger import logging
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.constants.training_pipeline import TARGET_COLUMN
from networksecurity.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact
)
from networksecurity.entity.cinfig_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.utils.mail_utils.utils import save_numpy_array_data, save_object
class DataTransformation:
    def __init__(self,
                 data_validation_artiifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig
    
    ):
        try:
            self.data_validation_artiifact:DataValidationArtifact=data_validation_artiifact
            self.data_transformaation_config=DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def get_data_transformer_object(self)->Pipeline:
        """
        it initialises a KNN objext with the parameters specified in the training_pipeline file
        and reurns a pipeline object with the KNNImputer object as the first step

        Args:
        cls:DataTransformation class
        returns:
        A pipeline object
        """
        logging.info("entered the get_data_transformer_object method of DataTransformation class"
        )
        try:
           imputer:KNNImputer= KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
           logging.info(f"initialised KNNImputer with parameters: {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
           processor:Pipeline=Pipeline([("imputer",imputer)])
           return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("Entered the initiate_data_transformation method of DataTransformation class")
            #reading train and test file path
            train_df=DataTransformation.read_data(self.data_validation_artiifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artiifact.valid_test_file_path)
            #training dataframe'
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_train_df=target_feature_train_df.replace(-1, 0)

            #testing dataframe
            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(-1, 0)

            preprocessor=self.get_data_transformer_object()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_feature_train_df=preprocessor_object.transform(input_feature_train_df)
            transformed_input_feature_test_df=preprocessor_object.transform(input_feature_test_df)

            train_arr=np.c_[transformed_input_feature_train_df,np.array(target_feature_train_df) ]
            test_arr=np.c_[transformed_input_feature_test_df,np.array(target_feature_test_df) ]

            #save numpy array data
            save_numpy_array_data(self.data_transformaation_config.transformed_train_file_path,train_arr)
            save_numpy_array_data(self.data_transformaation_config.transformed_test_file_path,test_arr)
            save_object(self.data_transformaation_config.transformed_object_file_path,preprocessor_object)


            #preparing artifacts
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformaation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformaation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformaation_config.transformed_test_file_path
            )
            return data_transformation_artifact


        except Exception as e:
            raise NetworkSecurityException(e,sys)