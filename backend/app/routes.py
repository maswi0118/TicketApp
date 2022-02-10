import base64
import os
import requests
from flask_cors import cross_origin
from flask import render_template, flash, redirect, request
from . import app
import json

token = ''


@app.route('/admin_panel', methods=['POST', 'GET'])
def admin():
    return render_template('admin.html')


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
        aid = add(form.name.data, form.genre.data, form.nationality.data, form.about.data)
        if aid:
            return redirect(f'/add_artist/{aid}')
        else:
            flash(f'Nie udało się dodać {form.name.data}, {form.nationality.data}.')
    return render_template('add_template.html', form=form)


@app.route('/add_artist/<aid>', methods=['POST', 'GET'])
def add_artist_image(aid: int):
    from .database import get_artists, set_image
    import urllib.request, json
    from .forms import ImageSelect
    artist_name = get_artists(aid)
    hrefs = []
    with urllib.request.urlopen(f'http://127.0.0.1:5000/artists/{artist_name.replace(" ", "+")}') as url:
        data = json.loads(url.read().decode())
        for item in data['artists']['items']:
            try:
                hrefs.append(item['images'][0]['url'])
            except IndexError:
                hrefs.append('../static/images/noImage.png')

    form = ImageSelect()
    form.number.choices = list(range(len(hrefs)))
    if form.validate_on_submit():
        set_image(aid, hrefs[int(form.number.data)])
        flash(f'Poprawnie dodano: {artist_name}.')
        return redirect('/admin_panel')
    return render_template('aritstst_img.html', form=form, hrefs=hrefs, n=len(hrefs))


@app.route('/add_event_province', methods=['POST', 'GET'])
def add_event_province():
    from .forms import SelectProvince
    form = SelectProvince()
    if form.validate_on_submit():
        return redirect(f'/add_event_city/{form.province.data}')
    return render_template('add_template.html', form=form)


@app.route('/add_event_city/<province>', methods=['POST', 'GET'])
def add_event_city(province):
    from .forms import SelectCity
    from .database import get_cities
    form = SelectCity()
    form.city.choices = get_cities(province)
    if form.validate_on_submit():
        return redirect(f'/add_event/{form.city.data}')
    return render_template('add_template.html', form=form)


@app.route('/add_event/<city>', methods=['POST', 'GET'])
def add_event(city):
    from .forms import AddEventForm
    from .database import add_event as add, get_cid, get_locations
    cid = get_cid(city)
    form = AddEventForm()
    form.location.choices = get_locations(cid)
    if form.validate_on_submit():
        print(form.date.data)
        if add(form.name.data, form.date.data, form.price.data, form.location.data, form.artist.data):
            flash(f'Poprawnie dodano wydarzenie {form.name.data}')
        else:
            flash(f'Nie udało dodać się wydarzenia {form.name.data}')
    return render_template('add_template.html', form=form)


@app.route('/get_events/<name>')
def get_events(name: str):
    from .database import get_events
    return json.dumps(get_events(name))


@app.route('/get_events/')
def get_all_events():
    from .database import get_events
    return json.dumps(get_events())


@app.route('/auth/register/<username>/<password>/<email>/<firstname>/<lastname>/<phone_number>', methods=['POST'])
def register(username, password, email, firstname, lastname, phone_number):
    from .database import add_user
    return add_user(username, password, email, firstname, lastname, phone_number)


@app.route('/auth/login/<username>/<password>', methods=['POST'])
def login(username, password):
    from .database import login_user
    return login_user(username, password)


@app.route('/ticket/<eid>/<uid>', methods=['POST'])
def ticket(eid: str, uid: str):
    from .database import add_ticket
    return add_ticket(uid, eid)


@app.route('/get_tickets/<uid>')
def get_tickets(uid: str):
    from .database import get_tickets as get
    return json.dumps(get(uid))
