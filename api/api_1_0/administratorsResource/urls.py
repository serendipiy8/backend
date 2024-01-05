#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request

from . import administrators_blueprint
from api_1_0.administratorsResource.administratorsResource import AdministratorsResource
from api_1_0.administratorsResource.administratorsOtherResource import AdministratorsOtherResource

api = Api(administrators_blueprint)

api.add_resource(AdministratorsResource, '/administrators/<AdminID>', '/Administrators', endpoint='Administrators')

@administrators_blueprint.route('/administrators', methods=['POST','PUT','GET','DELETE'], endpoint='administrators')
def administrators():
    if request.method=='GET':
        return AdministratorsOtherResource.administrators_query()
    if request.method=='POST':
        return AdministratorsOtherResource.administrators_post()
    if request.method=='DELETE':
        return AdministratorsOtherResource.administrators_delete()
    if request.method=='PUT':
        return AdministratorsOtherResource.administrators_revise()