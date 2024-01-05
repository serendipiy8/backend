#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import refunds_blueprint
from api_1_0.refundsResource.refundsResource import RefundsResource
from api_1_0.refundsResource.refundsOtherResource import RefundsOtherResource

api = Api(refunds_blueprint)

api.add_resource(RefundsResource, '/refunds/<RefundID>', '/Refunds', endpoint='Refunds')

@refunds_blueprint.route('/refunds', methods=['POST','PUT','GET'], endpoint='refunds')
def refunds():
    if request.method=='GET':
        return RefundsOtherResource.refunds_query()
    if request.method=='POST':
        return RefundsOtherResource.refunds_post()
    if request.method=='PUT':
        return RefundsOtherResource.refunds_revise()

@refunds_blueprint.route('/refundsOrder',methods=['GET'],endpoint='refundsOrder')
def refundsOrder():
    return RefundsOtherResource.refundsOrder()