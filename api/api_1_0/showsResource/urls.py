#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import shows_blueprint
from api_1_0.showsResource.showsResource import ShowsResource
from api_1_0.showsResource.showsOtherResource import ShowsOtherResource

api = Api(shows_blueprint)

api.add_resource(ShowsResource, '/shows/<ShowID>', '/shows', endpoint='Shows')

