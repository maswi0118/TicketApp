from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123'
CORS(app)

from . import routes

