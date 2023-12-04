# coding: utf-8
from . import db, BaseModel


class Ticketprices(BaseModel):
    __tablename__ = 'ticketprices'

    TicketID = db.Column(db.Integer, primary_key=True)
    ShowID = db.Column(db.Integer)
    Price = db.Column(db.Numeric(10, 2))
    Category = db.Column(db.String(255))
    TotalQuantity = db.Column(db.Integer)
    RemainingQuantity = db.Column(db.Integer)
