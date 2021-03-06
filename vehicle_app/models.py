from vehicle_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(280), nullable=False)
    vehicles = db.relationship('Vehicle', back_populates='manufacturer')

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(280), nullable=False)
    vin = db.Column(db.String(280), nullable=False)
    
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
    manufacturer = db.relationship('Manufacturer', back_populates='vehicles')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
