# coding: utf-8
from . import db, BaseModel


class Theaters(BaseModel):
    __tablename__ = 'theaters'

    TheaterID = db.Column(db.Integer, primary_key=True)
    TheaterName = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    Capacity = db.Column(db.Integer)
    AdminID = db.Column(db.Integer)
