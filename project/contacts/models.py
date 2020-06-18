# contacts models
from project import db

class Contacts(db.Model):
    # sno , name , email , phone_no , msg , date #db variables
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120), nullable=True)
