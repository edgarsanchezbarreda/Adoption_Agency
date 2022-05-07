from models import db, Pet, default_image
from app import app

db.drop_all()
db.create_all()


Dante = Pet(name = 'Dante', species = 'Dog', photo_url = 'https://i0.wp.com/moviepaws.com/wp-content/uploads/2017/11/coco-dante1.jpg?resize=700%2C358&ssl=1', age = 3, notes = 'Dante is a Xolo breed that is very silly and good with kids.', available = True)

Pumba = Pet(name = 'Pumba', species = 'Boar', photo_url = 'https://www.drawinghowtodraw.com/stepbystepdrawinglessons/wp-content/uploads/2011/03/finished-pumba-lion-king-color.png', age = 10, notes = 'Pumba is a boar that is very fun and jolly.', available = False)

Dory = Pet(name = 'Dory', species = 'Pacific Blue Tang', photo_url = 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F14%2F2016%2F03%2F31%2F033116-finding-dory.jpg', age = 5, notes = 'Dory is a very friendly but forgetful fish', available = True)

db.session.add_all([Dante, Pumba, Dory])
db.session.commit()