import os
import sys
import pandas as pd
import pymongo
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
print(f"MongoDB URI: {MONGO_DB_URI}")


import certifi
ca = certifi.where() #it will give you the path to the certificate bundle


from Exception.exception import NetworkSecurityException
from Custom_logging import logger
import json


class NetworkDataSecurity:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(error_message=str(e), error_detail=sys)
        
        
    def csv_to_json_convertor(self, file_path: str) -> list:
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            #mongoDB only accepts list of dictionaries to insert data into the collection
            records = list(json.loads(df.T.to_json()).values())
            return records            
        except Exception as e:
            raise NetworkSecurityException(error_message=str(e), error_detail=sys)
        
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(error_message=str(e), error_detail=sys)
            
            
if __name__ == "__main__":
    FILE_PATH = os.path.join(BASE_DIR, "Network_Data", "phisingData.csv")
    DATABASE_NAME = "Vijay_NetworkSecurityDB"
    COLLECTION_NAME = "NetworkData"
    network_obj = NetworkDataSecurity()
    records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)
    print(f"Number of records to be inserted into MongoDB collection: {records}")
    no_of_records = network_obj.insert_data_to_mongodb(records=records, database=DATABASE_NAME, collection=COLLECTION_NAME) 
    print(f"Number of records inserted into MongoDB collection: {no_of_records}")
    
    
    
    