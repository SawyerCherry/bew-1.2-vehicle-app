from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class NewVehicleForm(FlaskForm):
    manufacturer_name = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    model = StringField('Model', validators=[DataRequired(), Length(min=1, max=280)])
    vin = StringField('VIN', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Submit')
