import pymongo
from mongo_db.db_settings import MongoSettings
from typing import List
from loguru import logger
import json

from pymongo.errors import WriteError, InvalidDocument

CONNECTION_STRING = "mongodb://{}:{}@{}:{}".format(MongoSettings.MONGO_USER, MongoSettings.MONGO_PASSWD,
                                                   MongoSettings.MONGO_HOST, int(MongoSettings.MONGO_PORT))

db_client = pymongo.MongoClient(CONNECTION_STRING)
mongo_db = db_client[MongoSettings.MONGO_DATABASE]
collection = mongo_db[MongoSettings.MONGO_COLLECTION]

def ingest_data_to_mongo(path_json_file: str) -> dict:
    """
    Ingests Scrapped data into MongoDB
    Args:
        path_json_file(str): this string is the exact path of the json file containing the product information

    """

    with open(path_json_file, 'r') as file:
        scrapped_data = json.load(file)
    try:
        inserted_docs = collection.insert_many(scrapped_data)
        logger.info("Documents succesfully inserted, ids are: {}".format(inserted_docs.inserted_ids))
    except WriteError as error:
        logger.error(str(error))
    except InvalidDocument as error:
        logger.error(str(error))
        logger.error("Please check that all the scrapped documents contain the same fields")



