from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, IntegerField, DateField

class AddCityForm(FlaskForm):
    city = StringField('Dodaj nowe miasto do bazy danych:')
    province = StringField('W jakim województwie znajduje się miasto?')
    submit = SubmitField('Zatwierdź')

class AddLocationForm(FlaskForm):
    from .database import get_cities
    name = StringField('Jak nazywa się obiekt?')
    city = SelectField('Wybierz miasto w którym znajduje się ten obiekt:', choices=get_cities())
    capacity = IntegerField('Jaka jest maksymalna pojemność tego obiektu?')
    address = TextAreaField('Jaki jest dokładny adres obiektu?')
    indoor = BooleanField('Czy obiekt jest zadaszony?')
    submit = SubmitField('Zatwierdź')

class AddArtistForm(FlaskForm):
    name = StringField('Jak nazywa się artysta?')
    genre = StringField('Jaki gatunek muzyczny wykonuje artysta?')
    nationality = StringField('Skąd pochodzi artysta?')
    about = TextAreaField('Krótko opisz artyste')
    submit = SubmitField('Zatwierdź')

class AddEventForm(FlaskForm):
    from .database import get_artists, get_locations
    name = StringField('Jak nazywa się wydarzenie?')
    date = DateField('Kiedy odbędzie się wydarzenie?')
    limit = IntegerField('Jaki jest limit osób na tym wydarzeniu?')
    location = SelectField('W którym obiekcie będzie miało miejsce wydarzenie?', choices=get_locations())
    artist = SelectField('Jaki artysta wystąpi?', choices=get_artists())
    submit = SubmitField('Zatwierdź')