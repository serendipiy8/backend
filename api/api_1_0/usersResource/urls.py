#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from flask import request
from . import users_blueprint
from api_1_0.usersResource.usersResource import UsersResource
from api_1_0.usersResource.usersOtherResource import UsersOtherResource

api = Api(users_blueprint)

api.add_resource(UsersResource, '/users/<UserID>', '/Users', endpoint='Users')


@users_blueprint.route('/users/login', methods=['POST'], endpoint='login')
def login():
    return UsersOtherResource.login()


@users_blueprint.route('/users/register', methods=['POST'], endpoint='register')
def register():
    return UsersOtherResource.register()

@users_blueprint.route('/users/information',methods=['PUT','GET'],endpoint='information')
def information():
    if request.method=='PUT':
        return UsersOtherResource.information_post()
    if request.method=='GET':
        return UsersOtherResource.information_query()