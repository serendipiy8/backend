#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import shows_blueprint
from api_1_0.showsResource.showsResource import ShowsResource
from api_1_0.showsResource.showsOtherResource import ShowsOtherResource

api = Api(shows_blueprint)

api.add_resource(ShowsResource, '/shows/<ShowID>', '/Shows', endpoint='Shows')

@shows_blueprint.route('/shows/adminpost', methods=['POST'], endpoint='adminpost')
def adminpost():
    return ShowsOtherResource.adminpost()

@shows_blueprint.route('/shows/queryShowID', methods=['GET'], endpoint='queryShowID')
def queryShowID():
    return ShowsOtherResource.queryShowID()

@shows_blueprint.route('/shows/queryShowName', methods=['GET'], endpoint='queryShowName')
def queryShowName():
    return ShowsOtherResource.queryShowName()

@shows_blueprint.route('/shows/queryITheaterID', methods=['GET'], endpoint='queryITheaterID')
def queryITheaterID():
    return ShowsOtherResource.queryITheaterID()

@shows_blueprint.route('/shows/adminadvise', methods=['PUT'], endpoint='adminadvise')
def adminadvise():
    return ShowsOtherResource.adminadvise()

@shows_blueprint.route('/shows/admindelete', methods=['DEL'], endpoint='admindelete')
def admindelete():
    return ShowsOtherResource.admindelete()
