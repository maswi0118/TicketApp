import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, IntegerField, \
    DecimalField, DateTimeLocalField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, ValidationError


class AddCityForm(FlaskForm):
    city = StringField('Dodaj nowe miasto do bazy danych:',
                       validators=[DataRequired(message='To pole nie może być puste')])
    province = StringField('W jakim województwie znajduje się miasto?',
                           validators=[DataRequired(message='To pole nie może być puste')])
    submit = SubmitField('Zatwierdź')


class AddLocationForm(FlaskForm):
    name = StringField('Jak nazywa się obiekt?', validators=[DataRequired(message='To pole nie może być puste')])
    city = SelectField('Wybierz miasto w którym znajduje się ten obiekt:')
    capacity = IntegerField('Jaka jest maksymalna pojemność tego obiektu?',
                            validators=[DataRequired(message='To pole nie może być puste'),
                                        NumberRange(min=0, message='Pojemność nie może być ujemna')])
    address = TextAreaField('Jaki jest dokładny adres obiektu?',
                            validators=[DataRequired(message='To pole nie może być puste')])
    indoor = BooleanField('Czy obiekt jest zadaszony?')
    submit = SubmitField('Zatwierdź')


class AddArtistForm(FlaskForm):
    name = StringField('Jak nazywa się artysta?', validators=[DataRequired(message='To pole nie może być puste')])
    genre = StringField('Jaki gatunek muzyczny wykonuje artysta?',
                        validators=[DataRequired(message='To pole nie może być puste')])
    nationality = StringField('Skąd pochodzi artysta?', validators=[DataRequired(message='To pole nie może być puste')])
    about = TextAreaField('Krótko opisz artyste', validators=[DataRequired(message='To pole nie może być puste')])
    submit = SubmitField('Zatwierdź', validators=[DataRequired(message='To pole nie może być puste')])


class AddEventForm(FlaskForm):
    name = StringField('Jak nazywa się wydarzenie?', validators=[DataRequired(message='To pole nie może być puste')])
    date = DateTimeLocalField('Kiedy odbędzie się wydarzenie?', format='%Y-%m-%dT%H:%M',
                              validators=[DataRequired(message='To pole nie może być puste')])
    price = DecimalField('Ile będzie kosztował bilet na wydarzenie?',
                         validators=[DataRequired(message='To pole nie może być puste'),
                                     NumberRange(min=0, message='Cena nie może być ujemna')])
    location = SelectField('W którym obiekcie będzie miało miejsce wydarzenie?')
    artist = SelectField('Jaki artysta wystąpi?')
    submit = SubmitField('Zatwierdź')

    def validate_date(self, field):
        if field.data < datetime.datetime.now():
            raise ValidationError('Nie można dodawać wydarzeń w przeszłości')


class SelectProvince(FlaskForm):
    province = SelectField('Wybierz województwo')
    submit = SubmitField('Zatwierdź')


class SelectCity(FlaskForm):
    city = SelectField('Wybierz miasto')
    submit = SubmitField('Zatwierdź')


class ImageSelect(FlaskForm):
    number = SelectField('Które zdjęcie pasuje do tego artysty?')
    submit = SubmitField('Zatwierdź')


class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(message='To pole nie może być puste'),
                                                            Regexp(r'^[\w.@+-]+$',
                                                                   message='Nazwa użytkownika może zawierać znaki alfanumeryczne oraz .@+-')])
    password = PasswordField('Hasło', validators=[DataRequired(message='To pole nie może być puste'),
                                                  Length(min=8, message='Hasło musi mieć przynajmniej 8 znaków'),
                                                  Regexp(r'^[\w.@+-]+$',
                                                         message='Hasło może zawierać znaki alfanumeryczne oraz .@+-')])
    submit = SubmitField('Zatwierdź')


class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(message='To pole nie może być puste'),
                                                            Regexp(r'^[\w.@+-]+$',
                                                                   message='Nazwa użytkownika może zawierać znaki alfanumeryczne oraz .@+-')])
    password = PasswordField('Hasło', validators=[DataRequired(message='To pole nie może być puste'),
                                                  Length(min=8, message='Hasło musi mieć przynajmniej 8 znaków'),
                                                  Regexp(r'^[\w.@+-]+$',
                                                         message='Hasło może zawierać znaki alfanumeryczne oraz .@+-')])
    password2 = PasswordField('Potwierdź hasło', validators=[DataRequired(message='To pole nie może być puste'),
                                                             Length(min=8,
                                                                    message='Hasło musi mieć przynajmniej 8 znaków'),
                                                             Regexp(r'^[\w.@+-]+$',
                                                                    message='Hasło może zawierać znaki alfanumeryczne oraz .@+-')])
    submit = SubmitField('Zatwierdź')


class DeleteForm(FlaskForm):
    to_delete = SelectField()
    submit = SubmitField('Zatwierdź')
