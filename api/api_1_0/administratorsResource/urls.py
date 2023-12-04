#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import administrators_blueprint
from api_1_0.administratorsResource.administratorsResource import AdministratorsResource
from api_1_0.administratorsResource.administratorsOtherResource import AdministratorsOtherResource

api = Api(administrators_blueprint)

api.add_resource(AdministratorsResource, '/administrators/<AdminID>', '/administrators', endpoint='Administrators')

