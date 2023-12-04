# coding: utf-8
from . import db, BaseModel


class Shows(BaseModel):
    __tablename__ = 'shows'

    ShowID = db.Column(db.Integer, primary_key=True)
    TheaterID = db.Column(db.Integer)
    ShowName = db.Column(db.String(255))
    Description = db.Column(db.Text)
    ShowDate = db.Column(db.Date)
    Duration = db.Column(db.Integer)
    AdminID = db.Column(db.Integer)
    Image = db.Column(db.String(255))
    Category = db.Column(db.String(255))
    City = db.Column(db.String(255))
