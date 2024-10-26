#we have 3 routes 
#1. One for signup
#2. One for signin
#3. One for Currency Conversion

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User , CurrencyConversion
from app import db



