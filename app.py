from operator import methodcaller
from flask import Flask, render_template, redirect
from models import db, connect_db, pg_user, pg_pwd, Pet
from forms import PetForm
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{username}:{password}@localhost:5432/adoption_db".format(username=pg_user, password=pg_pwd)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'welcomehomesir'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=True


connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/pets/new', methods=['GET','POST'])
def new_pet_form():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet_form.html', form=form)

@app.route('/pets/<pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    pet = Pet.query.get(pet_id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form)