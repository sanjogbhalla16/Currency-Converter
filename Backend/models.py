#this will show how are schema looks like in the database

from flask import SQLAlchemy

#This line creates an instance of SQLAlchemy, which will manage the connection to the database. 
# By calling db = SQLAlchemy(), you set up db as the primary way to interact with the database throughout the app.
db = SQLAlchemy()

# we have 2 tables, one is for user and other is for currency conversion rate

class User(db.Model()):
    __tablename__ ='users'
     #this will create a table in our database with the name of 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(12), unique = True)
    
    
class CurrencyConversion(db.Model()):
    __tablename__ = 'currency_conversions'
    #this will create a table in our database with the name of 'currency_rate'
    id = db.Column(db.Integer, primary_key = True)
    from_currency = db.Column(db.String(4), unique = True, nullable = False)
    to_currency = db.Column(db.String(4), unique = True, nullable = False)
    amount = db.Column(db.Float, unique = False, nullable = False)
    converted_amount = db.Column(db.Float, unique = False,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    #a one-to-many relationship between the CurrencyConversion and User models in SQLAlchemy
    user = db.relationship('User', backref = db.backref('conversion', lazy = True))
    
    
