#we have 3 routes 
#1. One for signup
#2. One for signin
#3. One for Currency Conversion

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User , CurrencyConversion
from app import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods = ['POST']) #these are the decorator functions
def signup():
    data = request.get_json()
    username = data.get(username)
    password = data.get(password)
    
    #check for the user password authentication
    user = User.query.filer_by(username = username).first()
    if not user or user.check_password_hash(user.password,password):
        return jsonify({'message': 'Password Incorrect'}), 401 
        #401 is the status code for unauthorized access




