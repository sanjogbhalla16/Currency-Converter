from pymongo import MongoClient
from config import Config

#using pymongo we are creating a connection to the database
#and taking the URL from config file
#db = client["ytmanager"] same same 
client = MongoClient(Config.MONGO_URI) #instance cluster 

db = client["currency_db"] #collection 
user_collection = db["users"]
book_collection = db["books"]

#print(user_collection)