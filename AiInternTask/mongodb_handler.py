from pymongo import MongoClient
import logging

class MongoDBHandler:
    def __init__(self, db_name="pdf_summarizer", collection_name="pdf_data"):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
        except Exception as e:
            logging.error(f"Error connecting to MongoDB: {e}")

    def update_document(self, pdf_url, metadata):
        try:
            self.collection.update_one({"pdf_url": pdf_url}, {"$set": metadata}, upsert=True)
            logging.info(f"MongoDB updated for {pdf_url}")
        except Exception as e:
            logging.error(f"Error updating MongoDB for {pdf_url}: {e}")
