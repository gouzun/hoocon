from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Mthlysalaryrecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(20))
    salarydate = db.Column(db.String(7))
    projectlocation = db.Column(db.String(50))    
    d1 = db.Column(db.Integer)
    d2 = db.Column(db.Integer)
    d3 = db.Column(db.Integer)
    d4 = db.Column(db.Integer)
    d5 = db.Column(db.Integer)
    d6 = db.Column(db.Integer)
    d7 = db.Column(db.Integer)
    d8 = db.Column(db.Integer)
    d9 = db.Column(db.Integer)
    d10 = db.Column(db.Integer)
    d11 = db.Column(db.Integer)
    d12 = db.Column(db.Integer)
    d13 = db.Column(db.Integer)
    d14 = db.Column(db.Integer)
    d15 = db.Column(db.Integer)
    d16 = db.Column(db.Integer)
    d17 = db.Column(db.Integer)
    d18 = db.Column(db.Integer)
    d19 = db.Column(db.Integer)
    d20 = db.Column(db.Integer)
    d21 = db.Column(db.Integer)
    d22 = db.Column(db.Integer)
    d23 = db.Column(db.Integer)
    d24 = db.Column(db.Integer)
    d25 = db.Column(db.Integer)
    d26 = db.Column(db.Integer)
    d27 = db.Column(db.Integer)
    d28 = db.Column(db.Integer)
    d29 = db.Column(db.Integer)
    d30 = db.Column(db.Integer)
    d31 = db.Column(db.Integer)
    totalhr = db.Column(db.Float(10,2))#35
    dayrate = db.Column(db.Float(10,2))#36
    hrrate = db.Column(db.Float(10,2))#37
    totalcost = db.Column(db.Float(10,2))#38
    datecreated = db.Column(db.DateTime(timezone=True), default=func.now())#39

