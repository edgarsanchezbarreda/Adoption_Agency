from models import db, Pet, default_image
from app import app

db.drop_all()
db.create_all()


Dante = Pet(name = 'Dante', species = 'Dog', photo_url = 'https://i0.wp.com/moviepaws.com/wp-content/uploads/2017/11/coco-dante1.jpg?resize=700%2C358&ssl=1', age = 3, notes = 'Dante is a Xolo breed that is very silly and good with kids.', available = True)

Felix = Pet(name = 'Felix', species = 'Cat', photo_url = 'https://cdn.onebauer.media/one/empire-legacy/uploaded/felix-the-cat-cartoon.jpg?format=jpg&quality=80&width=1800&ratio=16-9&resize=aspectfill', age = 10, notes = 'Felix is a cat that is very fun and jolly.', available = False)

Sonic = Pet(name = 'Sonic', species = 'Porcupine', photo_url = 'https://i.ebayimg.com/images/g/opkAAOSwXtNafFAa/s-l500.jpg', age = 5, notes = 'Sonic is a very VERY fast porcupine', available = True)

db.session.add_all([Dante, Felix, Sonic])
db.session.commit()