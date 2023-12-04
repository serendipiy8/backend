# coding: utf-8
from . import db, BaseModel


class Users(BaseModel):
    __tablename__ = 'users'

    UserID = db.Column(db.BigInteger, primary_key=True)
    UserName = db.Column(db.String(255), nullable=True)
    RealName = db.Column(db.String(255), nullable=True)
    Gender = db.Column(db.String(10), nullable=True)
    IDCard = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(255), nullable=True)
    Address = db.Column(db.String(255), nullable=True)
    Account = db.Column(db.String(255), nullable=True)
    Password = db.Column(db.String(255), nullable=True)
