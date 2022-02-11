import datetime

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from .database import check_if_is_over

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123'
CORS(app)

sched = BackgroundScheduler(daemon=True)
sched.add_job(check_if_is_over, 'interval', minutes=60)
sched.start()

from . import routes
