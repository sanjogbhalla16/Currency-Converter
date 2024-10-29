#this will the main file for backend
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes import auth

app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)


# Register Blueprints
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(debug=True)
