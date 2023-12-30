#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import theaters_blueprint
from api_1_0.theatersResource.theatersResource import TheatersResource
from api_1_0.theatersResource.theatersOtherResource import TheatersOtherResource

api = Api(theaters_blueprint)

api.add_resource(TheatersResource, '/Theaters/<TheaterID>', '/Theaters', endpoint='Theaters')

@theaters_blueprint.route('/theaters', methods=['POST','PUT','GET','DELETE'], endpoint='theaters')
def theaters():
    if request.method=='GET':
        return TheatersOtherResource.theaters_query()
    if request.method=='POST':
        return TheatersOtherResource.theaters_post()
    if request.method=='DELETE':
        return TheatersOtherResource.theaters_delete()
    if request.method=='PUT':
        return TheatersOtherResource.theaters_revise()
