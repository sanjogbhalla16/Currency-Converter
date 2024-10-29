from pymongo import MongoClient
from config import Config

#db = client["ytmanager"] same same 
client = MongoClient(Config.MONGO_URI)

db = client["currency_db"]
user_collection = db["users"]
