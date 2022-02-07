from .models import *
from . import admin
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(City, db.session))