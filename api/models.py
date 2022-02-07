from api import db
from datetime import datetime
from sqlalchemy.inspection import inspect
class PersonModel(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(200) , nullable = False)
    Address = db.Column(db.String(200) , nullable = False)
    Phone = db.Column(db.String(13),nullable = False)
    created = db.Column(db.DateTime , default = datetime.utcnow)
    