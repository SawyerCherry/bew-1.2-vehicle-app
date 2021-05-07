import os
from unittest import TestCase

from datetime import date
 
from vehicle_app import app, db, bcrypt
from vehicle_app.models import Manufacturer, User, Vehicle

