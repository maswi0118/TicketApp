import base64
import os
import requests
from flask_cors import cross_origin
from flask import render_template
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

@app.route('/add_city')
def add_city():
    from .forms import AddCityForm
    form = AddCityForm()
    return render_template('add_template.html', form=form)
