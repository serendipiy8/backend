# coding: utf-8
from . import db, BaseModel


class Refunds(BaseModel):
    __tablename__ = 'refunds'

    RefundID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer)
    AdminID = db.Column(db.Integer)
    RefundTime = db.Column(db.DateTime)
    RefundReason = db.Column(db.Text)
    TicketStatus = db.Column(db.String(20))
    OrderID = db.Column(db.Integer)
