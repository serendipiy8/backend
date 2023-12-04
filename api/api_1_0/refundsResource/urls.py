#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import refunds_blueprint
from api_1_0.refundsResource.refundsResource import RefundsResource
from api_1_0.refundsResource.refundsOtherResource import RefundsOtherResource

api = Api(refunds_blueprint)

api.add_resource(RefundsResource, '/refunds/<RefundID>', '/refunds', endpoint='Refunds')

