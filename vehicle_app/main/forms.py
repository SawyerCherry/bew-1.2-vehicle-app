from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from vehicle_app.models import Manufacturer, User, Vehicle

class VehicleForm(FlaskForm):
    
    model = StringField('Model', validators=[DataRequired(), Length(min=1, max=280)])
    vin = StringField('VIN', validators=[DataRequired(), Length(min=1, max=280)])
    manufacturer = QuerySelectField('Manufacturer',
        query_factory=lambda: Manufacturer.query, allow_blank=False)
    submit = SubmitField('Submit')

class ManufacturerForm(FlaskForm):
    """Form to enter Manufacturer for the vehicle."""
    name = StringField('Manufacturer Name',
        validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')
