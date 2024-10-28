#we have 3 routes 
#1. One for signup
#2. One for signin
#3. One for Currency Conversion
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
#from models import User , CurrencyConversion
#from app import db

auth_bp = Blueprint('auth', __name__)


#API for login
@auth_bp.route('/login', methods = ['POST']) #these are the decorator functions
def signin():
    data = request.get_json()
    username = data.get(username)
    password = data.get(password)
    
    #check for the user password authentication
    user = User.query.filer_by(username = username).first()
    if user and user.check_password_hash(user.password,password):
        access_token = create_access_token(identity=user.id)
        return jsonify ({'access_token': access_token}) , 200 
        #200 is the status code for successful request processing.    
    
    return jsonify({'message': 'Password Incorrect'}), 401 
        #401 is the status code for unauthorized access
        
        
#API for registration
@auth_bp.route('/register', methods = ['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))
    
    #create and add new user
    new_user = User(username=username, password=password)
    
    
    return jsonify({"message": "User registered successfully"}), 201
    




