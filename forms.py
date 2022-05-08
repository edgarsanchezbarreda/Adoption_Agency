from wsgiref.validate import validator
from flask_wtf import FlaskForm
from sqlalchemy import Float
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """This form is used to dynamically add forms to our HTML pages that relate to adding or displaying pet data."""
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices = [('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')], validate_choice=True)
    photo_url = StringField('Photo Url', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(max=30), Optional()])
    notes = StringField('Notes')
    available = BooleanField('Available', validators=[InputRequired()])

class EditPetForm(FlaskForm):
    """This form is used to display only the photo_url, notes, and availability data in our HTML page that allows us to edit each pet."""
    photo_url = StringField('Photo Url', validators=[URL(), Optional()])
    notes = StringField('Notes')
    available = BooleanField('Available', validators=[InputRequired()])