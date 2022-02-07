from . import db

class City(db.Model):
    __tablename__ = 'cities'
    city = db.VARCHAR(45)
    province = db.VARCHAR(45)