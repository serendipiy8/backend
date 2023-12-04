#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import theaters_blueprint
from api_1_0.theatersResource.theatersResource import TheatersResource
from api_1_0.theatersResource.theatersOtherResource import TheatersOtherResource

api = Api(theaters_blueprint)

api.add_resource(TheatersResource, '/theaters/<TheaterID>', '/theaters', endpoint='Theaters')

