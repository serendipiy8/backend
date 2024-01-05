#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import orders_blueprint
from api_1_0.ordersResource.ordersResource import OrdersResource
from api_1_0.ordersResource.ordersOtherResource import OrdersOtherResource

api = Api(orders_blueprint)

api.add_resource(OrdersResource, '/orders/<OrderID>', '/Orders', endpoint='Orders')

@orders_blueprint.route('/orders', methods=['POST','PUT','GET','DELETE'], endpoint='orders')
def orders():
    if request.method=='GET':
        return OrdersOtherResource.orders_query()
    if request.method=='POST':
        return OrdersOtherResource.orders_post()
    if request.method=='PUT':
        return OrdersOtherResource.orders_revise()

@orders_blueprint.route('orders/queryUser',methods=['GET'],endpoint='queryUser')
def queryUser():
    return  OrdersOtherResource.queryUser()