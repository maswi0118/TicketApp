import base64
import hashlib
import json
import os

import requests
from flask import render_template, flash, redirect, session
from flask_cors import cross_origin

from . import app

token = ''


def is_not_logged():
    return 'username' not in session.keys()


@app.route('/')
def index():
    if is_not_logged():
        return redirect('/login')
    else:
        return redirect('/admin_panel')


@app.route('/admin_panel', methods=['POST', 'GET'])
def admin_panel():
    if is_not_logged():
        return redirect('/login')
    return render_template('admin.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


@app.route('/add_city', methods=['POST', 'GET'])
def add_city():
    if is_not_logged():
        return redirect('/login')
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
    from .database import get_cities
    if is_not_logged():
        return redirect('/login')
    from .forms import AddLocationForm
    from .database import add_location as add
    form = AddLocationForm()
    form.city.choices = get_cities()
    if form.validate_on_submit():
        if add(form.name.data, form.capacity.data, form.address.data, form.indoor.data, form.city.data):
            flash(f'Poprawnie dodano: {form.name.data}, {form.address.data}.')
        else:
            flash(f'Nie udało się dodać {form.name.data}.')
    return render_template('add_template.html', form=form)


@app.route('/add_artist', methods=['POST', 'GET'])
def add_artist():
    if is_not_logged():
        return redirect('/login')
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
    if is_not_logged():
        return redirect('/login')
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
    if is_not_logged():
        return redirect('/login')
    from .forms import SelectProvince
    from .database import get_districts
    form = SelectProvince()
    form.province.choices = get_districts()
    if form.validate_on_submit():
        return redirect(f'/add_event_city/{form.province.data}')
    return render_template('add_template.html', form=form)


@app.route('/add_event_city/<province>', methods=['POST', 'GET'])
def add_event_city(province):
    if is_not_logged():
        return redirect('/login')
    from .forms import SelectCity
    from .database import get_cities
    form = SelectCity()
    form.city.choices = get_cities(province)
    if form.validate_on_submit():
        return redirect(f'/add_event/{form.city.data}')
    return render_template('add_template.html', form=form)


@app.route('/add_event/<city>', methods=['POST', 'GET'])
def add_event(city):
    from .database import get_artists
    if is_not_logged():
        return redirect('/login')
    from .forms import AddEventForm
    from .database import add_event as add, get_cid, get_locations
    cid = get_cid(city)
    form = AddEventForm()
    form.location.choices = get_locations(cid)
    form.artist.choices = get_artists()
    if form.validate_on_submit():
        if add(form.name.data, form.date.data, form.price.data, form.location.data, form.artist.data):
            flash(f'Poprawnie dodano wydarzenie {form.name.data}')
        else:
            flash(f'Nie udało dodać się wydarzenia {form.name.data}')
    return render_template('add_template.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def admin_login():
    from .forms import LoginForm
    from .database import get_admin
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = hashlib.sha256(form.password.data.encode()).hexdigest()
        admin = get_admin(username)
        if admin[2] == password and admin[3] == 1:
            session['username'] = username
            return redirect('/admin_panel')
    return render_template('add_template.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def admin_register():
    from .forms import RegisterForm
    from .database import add_admin
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data == form.password2.data:
            username = form.username.data
            password = hashlib.sha256(form.password.data.encode()).hexdigest()
            add_admin(username, password)
            return redirect('/login')
    return render_template('add_template.html', form=form)


@app.route('/add_money/<username>/<amount>')
def add_money(username: str, amount: int):
    from .database import add_money
    return str(add_money(username, amount)).lower()


@app.route('/delete_event', methods=['GET', 'POST'])
def delete_event():
    if is_not_logged():
        return redirect('/login')
    from .database import delete_event, get_events_names, get_eid
    from .forms import DeleteForm
    form = DeleteForm()
    form.to_delete.choices = get_events_names()
    form.to_delete.description = 'Wybierz event do usunięcia'
    if form.validate_on_submit():
        delete_event(get_eid(form.to_delete.data))
        flash(f'Poprawnie usunięto {form.to_delete.data}')
        return redirect('/admin_panel')
    return render_template('add_template.html', form=form)


@app.route('/delete_artist', methods=['GET', 'POST'])
def delete_artist():
    if is_not_logged():
        return redirect('/login')
    from .database import get_artists, delete_artist
    from .forms import DeleteForm
    form = DeleteForm()
    form.to_delete.choices = get_artists()
    form.to_delete.description = 'Wybierz artyste do usunięcia np. Sobela'
    if form.validate_on_submit():
        delete_artist(form.to_delete.data)
        flash(f'Poprawnie usunięto {form.to_delete.data}')
        return redirect('/admin_panel')
    return render_template('add_template.html', form=form)


# API

@app.route('/get_events/<name>')
@cross_origin()
def get_events(name: str):
    from .database import get_events as get
    return json.dumps(get(name))


@app.route('/get_events/')
@cross_origin()
def get_all_events():
    from .database import get_events
    return json.dumps(get_events())


@app.route('/auth/register/<username>/<password>/<email>/<firstname>/<lastname>/<phone_number>',
           methods=['POST', 'GET'])
@cross_origin()
def register(username, password, email, firstname, lastname, phone_number):
    from .database import add_user
    import hashlib
    return add_user(username, hashlib.sha256(password.encode()).hexdigest(), email, firstname, lastname, phone_number)


@app.route('/auth/login/<username>/<password>', methods=['GET'])
@cross_origin()
def login(username, password):
    from .database import login_user
    import hashlib
    return {"response": login_user(username, hashlib.sha256(password.encode()).hexdigest())}


@app.route('/ticket/<eid>/<username>', methods=['GET'])
@cross_origin()
def ticket(eid: str, username: str):
    from .database import add_ticket, get_uid
    uid = get_uid(username)
    return json.dumps(add_ticket(uid, eid))


@app.route('/get_tickets/<username>')
@cross_origin()
def get_tickets(username: str):
    from .database import get_tickets as get, get_uid
    uid = get_uid(username)
    return json.dumps(get(uid))


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

@app.route('/get_balance/<username>')
@cross_origin()
def get_balance(username: str):
    from .database import get_uid, get_balance
    data = get_balance(get_uid(username))
    return {'balance': data[0], 'email': data[1], 'phone': data[2]}
