import os
import unittest
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
    v1 = Manufacturer(name='Dodge')
    model1 = Vehicle(
        manufacturer=v1,
        vin='3GCUKREC8JG183079',
        model="2018 Silverado 1500 Z71 LT",
    )
    db.session.add(model1)

    v2 = Manufacturer(name="Ford Motor Company")
    model2 = Vehicle(
        manufacturer=v2,
        vin='1FTFW1EFOBKD18803',
        model="2011 Ford F150 Lariat"
    )
    db.session.add(model2)
    db.session.commit()

def create_manufacturer():
    m1 = Manufacturer(name='Tesla')
    db.session.add(m1)
    db.session.commit()
    
    

def create_user():
    # Creates a user with username 'sawyer' and password of 'password'
    password_hash = bcrypt.generate_password_hash('pass').decode('utf-8')
    user = User(username='sawyer', password=password_hash)
    db.session.add(user)
    db.session.commit()

class MainTests(unittest.TestCase):
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_create_vehicle(self):
        create_user()
        create_vehicle()

        login(self.app, 'sawyer', 'pass')

        vehicle_post = {
            "manufacturer": 1,
            "model": "1999 Ram 2500 12v",
            "vin": "JLKN0808LLY94872"
        }
        self.app.post('/create_vehicle', data=vehicle_post)

        vehicle_created = Vehicle.query.filter_by(model='1999 Ram 2500 12v').one()

        self.assertIsNotNone(vehicle_created)
        self.assertEqual(vehicle_created.manufacturer.name, 'Dodge')

    def test_create_manufacturer(self):
        """Test to see if we can create a manufacturer"""
        create_user()
        create_manufacturer()

        login(self.app, 'sawyer', 'pass')

        manufacturer_post = {
            "name": 3
        }
        self.app.post('/create_manufacturer', data=manufacturer_post)

        manufacturer_created = Manufacturer.query.filter_by(name='Tesla').one()
        self.assertIsNotNone(manufacturer_created)
        self.assertEqual(manufacturer_created.name, 'Tesla')

    def test_create_vehicle_logged_out(self):
        """see if the user is not able to create a vehicle unless they are logged in"""
        create_vehicle()
        create_user()
        response = self.app.get('/create_vehicle')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/login?next=%2Fcreate_vehicle', response.location)

    


    

        





