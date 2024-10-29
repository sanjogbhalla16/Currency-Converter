#we have 3 routes 
#1. One for signup
#2. One for signin
#3. One for Currency Conversion
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity
from database import user_collection

auth = Blueprint('auth', __name__)


#print(user_collection)

#API for login
@auth.route('/login', methods = ['POST']) #these are  the decorator functions
@jwt_required()
def signup():
    data = request.get_json()
    username = data.get(username)
    password = data.get(password)
    
    #check for the user password authentication
    user = user_collection.find_one(username)
    print(user)
    if user and check_password_hash(user.password,password):
        access_token = create_access_token(identity=user._id)
        return jsonify ({'access_token': access_token}) , 200 
        #200 is the status code for successful request processing.    
    
    return jsonify({'message': 'Password Incorrect'}), 401 
        #401 is the status code for unauthorized access
        
        
#API for registration
@auth.route('/register', methods = ['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))
    
    #create and add new user
    user_collection.insert_one(username=username, password=password)
    
    
    return jsonify({"message": "User registered successfully"}), 201
    

# Protected Route (requires authentication)
@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


