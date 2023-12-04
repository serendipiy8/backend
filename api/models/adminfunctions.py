# coding: utf-8
from . import db, BaseModel


class Adminfunctions(BaseModel):
    __tablename__ = 'adminfunctions'

    FunctionID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Permissions = db.Column(db.String(255))
