from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


default_image = 'https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png'

class Pet(db.Model):
    """This creates a 'Pet' class used to save data for each pet that is created and stored in the DB."""
    __tablename__ = 'pets'

    id = db.Column(
        db.Integer, 
        primary_key = True, 
        autoincrement = True)
    name = db.Column(
        db.Text, 
        nullable = False)
    species = db.Column(
        db.Text, 
        nullable = False)
    photo_url = db.Column(
        db.Text,
        nullable = True,
        default = default_image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True)
    