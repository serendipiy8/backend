#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import orders_blueprint
from api_1_0.ordersResource.ordersResource import OrdersResource
from api_1_0.ordersResource.ordersOtherResource import OrdersOtherResource

api = Api(orders_blueprint)

api.add_resource(OrdersResource, '/orders/<OrderID>', '/Orders', endpoint='Orders')

