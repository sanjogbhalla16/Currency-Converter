#we have 3 routes 
#1. One for signup
#2. One for signin
#3. One for Currency Conversion
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from database import user_collection
import requests

auth = Blueprint('auth', __name__)


#Route for registration
@auth.route('/register', methods = ['POST'])
@jwt_required
def signin():
    data = request.get_json()
    username = data.get('username')
    print(username)
    password = data.get('password')
    print(password)
    
    #create and add new user
    if user_collection.find_one({"username": username}):
         return jsonify({"message": "User already exists"}), 409
    
    hashed_password = generate_password_hash(password)
    user_collection.insert_one({"username": username, "password": hashed_password}) 
    return jsonify({"message": "User registered successfully"}), 201

#Route for login
@auth.route('/login', methods = ['POST']) #these are the decorator functions
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    #check for the user password authentication
    user = user_collection.find_one({"username":username})
    print(user)
    if user and check_password_hash(user["password"],password):
        access_token = create_access_token(identity=str(user["_id"]))
        return jsonify ({'access_token': access_token}) , 200 
        #200 is the status code for successful request processing.    
    return jsonify({'message': 'Password Incorrect'}), 401 
        #401 is the status code for unauthorized access
        
#Route for Currency conversion
@auth.route('/convert',methods = ['POST'])
def Converter():
    data = request.get_json()
    amount = data.get('amount')
    code = data.get('code')
    url = 'https://v6.exchangerate-api.com/v6/0fe7602e3c578f26d5d18b52/latest/USD'
    response = requests.get(url).json()
    
    if response["result"]:
        curr_conversion = response["conversion_rates"]
        rate = curr_conversion.get(code)
        return f"The exchange rate from USD to {code} is {rate}."
    
    
        
        



