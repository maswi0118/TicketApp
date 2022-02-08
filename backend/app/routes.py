import base64
import os
import requests
from flask_cors import cross_origin
from flask import render_template, flash
from . import app


token = ''

@app.route('/artists/<name>')
@cross_origin()
def get_artists(name):
    global token
    try:
        res = requests.get(
            f'https://api.spotify.com/v1/search?q={name}&type=artist&limit=10&',
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
        if 399 < res.status_code < 500:
            token = get_token()
            res = requests.get(
                f'https://api.spotify.com/v1/search?q={name}&type=artist&limit=10&',
                headers={
                    "Authorization": f"Bearer {token}"
                }
            )
        return res.json()
    except:
        return "siema"


def get_token():
    message = os.getenv('CLIENT_ID') + ":" + os.getenv('CLIENT_SECRET')
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    res = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            "Authorization": f"Basic {base64_message}"
        },
        data={
            "grant_type": "client_credentials"
        })
    return res.json().get('access_token')

@app.route('/add_city', methods=['POST', 'GET'])
def add_city():
    from .forms import AddCityForm
    from .database import add_city as add
    form = AddCityForm()
    if form.validate_on_submit():
<<<<<<< HEAD
        return render_template('add_template.html', form=form)
=======
        if add(form.city.data, form.province.data):
            flash(f'Poprawnie dodano: {form.city.data}, {form.province.data}.')
        else:
            flash(f'Nie udało się dodać: {form.city.data}, {form.province.data}.')
    return render_template('add_template.html', form=form)


@app.route('/add_location', methods=['POST', 'GET'])
def add_location():
    from .forms import AddLocationForm
    from .database import add_location as add
    form = AddLocationForm()
    if form.validate_on_submit():
        if add(form.name.data, form.capacity.data, form.address.data, form.indoor.data, form.city.data):
            flash(f'Poprawnie dodano: {form.name.data}, {form.address.data}.')
        else:
            flash(f'Nie udało się dodać {form.name.data}.')
    return render_template('add_template.html', form=form)

@app.route('/add_artist', methods=['POST', 'GET'])
def add_artist():
    from .forms import AddArtistForm
    from .database import add_artist as add
    form = AddArtistForm()
    if form.validate_on_submit():
        if add(form.name.data, form.genre.data, form.nationality.data, form.about.data):
            flash(f'Poprawnie dodano: {form.name.data}, {form.nationality.data}.')
        else:
            flash(f'Nie udało się dodać {form.name.data}, {form.nationality.data}.')
    return render_template('add_template.html', form=form)

@app.route('/add_event', methods=['POST', 'GET'])
def add_event():
    from .forms import AddEventForm
    from .database import add_event as add
    form = AddEventForm()
    if form.validate_on_submit():
        if add(form.name.data, form.date.data, form.limit.data, form.location.data, form.artist.data):
            flash(f'Poprawnie dodano wydarzenie {form.name.data}')
        else:
            flash(f'Nie udało dodać się wydarzenia {form.name.data}')
    return render_template('add_template.html', form=form)
>>>>>>> 3176fabd32d8377c3eb94b74f7fedfa0190ac53a
