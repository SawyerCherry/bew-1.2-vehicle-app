import os
from unittest import TestCase

from datetime import date
 
from vehicle_app import app, db, bcrypt
from vehicle_app.models import Manufacturer, User, Vehicle

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_vehicle():
    a1 = Manufacturer(manufacturer_name='General Motors')
    b1 = Vehicle(
        vin='3GCUKREC8JG183079',
        model="2018 Silverado 1500 Z71 LT",
    )
    db.session.add(b1)

    a2 = Manufacturer(manufacturer_name="Ford Motor Company")
    b2 = Vehicle(
        vin='1FTFW1EFOBKD18803',
        model="2011 Ford F150 Lariat"
    )
    db.session.add(b2)
    db.session.commit()