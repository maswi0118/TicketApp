from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddCityForm(FlaskForm):
    city = StringField('Dodaj nowe miasto do bazy danych:')
    submit = SubmitField('Zatwierdź')