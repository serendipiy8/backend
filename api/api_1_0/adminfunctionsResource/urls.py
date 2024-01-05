#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import adminfunctions_blueprint
from api_1_0.adminfunctionsResource.adminfunctionsResource import AdminfunctionsResource
from api_1_0.adminfunctionsResource.adminfunctionsOtherResource import AdminfunctionsOtherResource

api = Api(adminfunctions_blueprint)

api.add_resource(AdminfunctionsResource, '/adminfunctions/<FunctionID>', '/Adminfunctions', endpoint='Adminfunctions')

@adminfunctions_blueprint.route('/adminfunctions', methods=['POST','PUT','DELETE'], endpoint='adminfunctions')
def adminfunctions():
    if request.method=='POST':
        return AdminfunctionsOtherResource.adminfunctions_post()
    if request.method=='DELETE':
        return AdminfunctionsOtherResource.adminfunctions_delete()
    if request.method=='PUT':
        return AdminfunctionsOtherResource.adminfunctions_revise()