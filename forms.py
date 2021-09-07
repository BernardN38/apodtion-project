from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, FloatField
from wtforms.fields.core import IntegerField, IntegerField
from wtforms.widgets.core import TextArea
from wtforms.validators import InputRequired,NumberRange,URL,AnyOf,Optional

class PetForm(FlaskForm):
    name = StringField('Pet Name')
    species = StringField('Pet Species',
                            validators=[AnyOf(values=['cat','dog','porcupine'])])
    photo_url = StringField('Picture URL',
                            validators=[URL(),Optional()])
    age = IntegerField('Pet Age',
                            validators=[NumberRange(min=0,max=30)])
    notes = StringField('Notes')