#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import adminfunctions_blueprint
from api_1_0.adminfunctionsResource.adminfunctionsResource import AdminfunctionsResource
from api_1_0.adminfunctionsResource.adminfunctionsOtherResource import AdminfunctionsOtherResource

api = Api(adminfunctions_blueprint)

api.add_resource(AdminfunctionsResource, '/adminfunctions/<FunctionID>', '/Adminfunctions', endpoint='Adminfunctions')

