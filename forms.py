from flask_wtf import FlaskForm
from sqlalchemy import Float
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices = [('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')], validate_choice=True)
    photo_url = StringField('Photo Url', validators=[URL()])
    age = IntegerField('Age', validators=[NumberRange(max=30)])
    notes = StringField('Notes')

