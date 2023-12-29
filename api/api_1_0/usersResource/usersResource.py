#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.usersController import UsersController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class UsersResource(Resource):

    # get
    @classmethod
    def get(cls, UserID=None):
        if UserID:
            kwargs = {
                'UserID': UserID
            }

            res = UsersController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('UserID', location='args', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('UserName', location='args', required=False, help='UserName参数类型不正确或缺失')
        parser.add_argument('RealName', location='args', required=False, help='RealName参数类型不正确或缺失')
        parser.add_argument('Gender', location='args', required=False, help='Gender参数类型不正确或缺失')
        parser.add_argument('IDCard', location='args', required=False, help='IDCard参数类型不正确或缺失')
        parser.add_argument('Email', location='args', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('Address', location='args', required=False, help='Address参数类型不正确或缺失')
        parser.add_argument('Account', location='args', required=False, help='Account参数类型不正确或缺失')
        parser.add_argument('Password', location='args', required=False, help='Password参数类型不正确或缺失')
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = UsersController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, UserID=None):
        if UserID:
            kwargs = {
                'UserID': UserID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = UsersController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, UserID):
        if not UserID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('UserName', location='form', required=False, help='UserName参数类型不正确或缺失')
        parser.add_argument('RealName', location='form', required=False, help='RealName参数类型不正确或缺失')
        parser.add_argument('Gender', location='form', required=False, help='Gender参数类型不正确或缺失')
        parser.add_argument('IDCard', location='form', required=False, help='IDCard参数类型不正确或缺失')
        parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('Address', location='form', required=False, help='Address参数类型不正确或缺失')
        parser.add_argument('Account', location='form', required=False, help='Account参数类型不正确或缺失')
        parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['UserID'] = UserID

        res = UsersController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        UsersList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('UsersList', type=str, location='form', required=False, help='UsersList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('UsersList'):
            kwargs['UsersList'] = json.loads(kwargs['UsersList'])
            for data in kwargs['UsersList']:
                for key in []:
                    data.pop(key, None)
            res = UsersController.add_list(**kwargs)

        else:
            parser.add_argument('UserID', location='form', required=True, help='UserID参数类型不正确或缺失')
            parser.add_argument('UserName', location='form', required=False, help='UserName参数类型不正确或缺失')
            parser.add_argument('RealName', location='form', required=False, help='RealName参数类型不正确或缺失')
            parser.add_argument('Gender', location='form', required=False, help='Gender参数类型不正确或缺失')
            parser.add_argument('IDCard', location='form', required=False, help='IDCard参数类型不正确或缺失')
            parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
            parser.add_argument('Address', location='form', required=False, help='Address参数类型不正确或缺失')
            parser.add_argument('Account', location='form', required=False, help='Account参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = UsersController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
