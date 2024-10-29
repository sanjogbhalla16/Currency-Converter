#this will the main file for backend
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes import auth


if __name__ == '__main__':
    app.run(debug=True)
