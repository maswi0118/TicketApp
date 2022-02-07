from flask import Flask
from flask_cors import CORS
from flask_admin import Admin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
admin = Admin(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123'


from . import routes, admin

