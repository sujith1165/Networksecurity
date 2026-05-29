import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)
           

    def insert_data_to_mongoDB(self, data, collection, database="NetworkSecurity"):
        try:
            self.database_name = database
            self.collection_name = collection

            self.collection = self.mongo_client[
                self.database_name
            ][
                self.collection_name
            ]

            self.collection.insert_many(data)

            return len(data)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__": 
    FILE_PATH = "Network_Data\phisingData.csv"     
    dATABASE="SUJITH_KUMAR"
    COLLECTION="networkdata"
    networkobj=NetworkDataExtract()
    data=networkobj.cv_to_json(file_path=FILE_PATH)
    print(data)
    no_of_records=networkobj.insert_data_to_mongoDB(data=data, collection=COLLECTION)
    print(f"Total number of records inserted to MongoDB are: {no_of_records}") 
