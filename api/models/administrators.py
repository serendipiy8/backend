# coding: utf-8
from . import db, BaseModel


class Administrators(BaseModel):
    __tablename__ = 'administrators'

    AdminID = db.Column(db.Integer, primary_key=True)
    AdminType = db.Column(db.String(20))
    Account = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Permissions = db.Column(db.String(255))
