#this will the main file for backend
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
#from flask_jwt_extended import JWTManager
# from config import Config
from routes import auth_bp
#from flask_cors import CORS

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for API requests
#CORS(app)


# Register Blueprints
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)
