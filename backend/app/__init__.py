from flask import Flask
from flask_cors import CORS
from flask_admin import Admin
from flask_migrate import Migrate

app = Flask(__name__)
admin = Admin(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = '41564645'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://s403025:4eqr87ckc1yk@labagh.pl:22/s403025'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from . import routes, admin

