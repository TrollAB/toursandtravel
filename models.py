from datetime import timezone
from enum import unique
from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class packages(db.Model):
    id = db.Column(db.Integer , primary_key  =True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone  = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(100), unique  = True)
    firstname = db.Column(db.String(100))
    
    password = db.Column(db.String(100))
 
    # packages = db.relationship('packages')
