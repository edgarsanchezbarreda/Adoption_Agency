from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] =  'helloworld123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def pet_list():
    """Renders the home page, that contains a list of all pets and a link to add a new pet."""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)


@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Renders the page to add new pets, and displays the forms to input all the required information to add a new pet. Also handles creating a new pet and adding it to our DB."""
    form = AddPetForm()

    if form.validate_on_submit():
        # If this form is validated, it takes the values from each form and uses them to create the new pet.
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        # If this form is not validated, then it simply renders the same page again.
        return render_template('add_pet_form.html', form = form)


@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def display_edit_pet(pet_id):
    """This route displays the edit page for each pet. Also, it handles editing the pet and submitting it to our DB."""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    edit_form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        # If the form is validated, the values from each form are used to edit the pet, committing it to the DB, and redirecting us to the homepage.
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        # If the form is not validated, than the page is rendered again.
        return render_template('display_edit_form.html', pet = pet, form = form, edit_form = edit_form)