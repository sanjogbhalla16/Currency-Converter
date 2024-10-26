#this will the main file for backend
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy 
# from flask_jwt_extended import JWTManager, jwt_required, current
# from config import Config

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'


if __name__ == '__main__':
    app.run(debug=True)
