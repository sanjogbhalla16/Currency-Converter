from pymongo import MongoClient
from config import Config

#using pymongo we are creating a connection to the database
#and taking the URL from config file
#db = client["ytmanager"] same same 
client = MongoClient(Config.MONGO_URI)

db = client["currency_db"]
user_collection = db["users"]

#print(user_collection)