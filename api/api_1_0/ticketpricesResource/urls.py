#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import ticketprices_blueprint
from api_1_0.ticketpricesResource.ticketpricesResource import TicketpricesResource
from api_1_0.ticketpricesResource.ticketpricesOtherResource import TicketpricesOtherResource

api = Api(ticketprices_blueprint)

api.add_resource(TicketpricesResource, '/ticketprices/<TicketID>', '/ticketprices', endpoint='Ticketprices')

