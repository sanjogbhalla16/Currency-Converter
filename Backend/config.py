import os

class Config():
      SECRET_KEY = os.getenv("SECRET_KEY", "yoursecretkey")
      MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sanjogbhalla:Cosmos1622@cluster0.achpb.mongodb.net/")