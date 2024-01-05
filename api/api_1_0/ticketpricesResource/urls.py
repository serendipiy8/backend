#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import ticketprices_blueprint
from api_1_0.ticketpricesResource.ticketpricesResource import TicketpricesResource
from api_1_0.ticketpricesResource.ticketpricesOtherResource import TicketpricesOtherResource

api = Api(ticketprices_blueprint)

api.add_resource(TicketpricesResource, '/ticketprices/<TicketID>', '/Ticketprices', endpoint='Ticketprices')

@ticketprices_blueprint.route('/ticketprices', methods=['POST','PUT','DEL','GET'], endpoint='ticketprices')
def ticketprices():
    if request.method=='POST':
        return TicketpricesOtherResource.ticketprices_post()
    if request.method=='DEL':
        return TicketpricesOtherResource.ticketprices_del()
    if request.method=='PUT':
        return TicketpricesOtherResource.ticketprices_put()
    if request.method=='GET':
        return TicketpricesOtherResource.ticketprices_query()

@ticketprices_blueprint.route('/TicketpricesQuery', methods=['GET'], endpoint='TicketpricesQuery')
def TicketpricesQuery():
    return TicketpricesOtherResource.ticketpricesQuery()