# coding: utf-8
from . import db, BaseModel


class Orders(BaseModel):
    __tablename__ = 'orders'

    OrderID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer)
    TicketID = db.Column(db.Integer)
    PurchaseTime = db.Column(db.DateTime)
    OrderStatus = db.Column(db.String(20))
    Quantity = db.Column(db.Integer)
