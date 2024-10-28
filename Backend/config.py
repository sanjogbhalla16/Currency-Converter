import os

class Config():
      SECRET_KEY = os.getenv("SECRET_KEY", "yoursecretkey")
      JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "yourjwtsecretkey")
      MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sanjogbhalla:Cosmos1622@cluster0.achpb.mongodb.net/")