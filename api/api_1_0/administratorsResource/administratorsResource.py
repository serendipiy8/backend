#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.administratorsController import AdministratorsController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class AdministratorsResource(Resource):

    # get
    @classmethod
    def get(cls, AdminID=None):
        if AdminID:
            kwargs = {
                'AdminID': AdminID
            }

            res = AdministratorsController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('AdminID', location='args', required=False, help='AdminID参数类型不正确或缺失')
        parser.add_argument('AdminType', location='args', required=False, help='AdminType参数类型不正确或缺失')
        parser.add_argument('Account', location='args', required=False, help='Account参数类型不正确或缺失')
        parser.add_argument('Password', location='args', required=False, help='Password参数类型不正确或缺失')
        parser.add_argument('Permissions', location='args', required=False, help='Permissions参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = AdministratorsController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, AdminID=None):
        if AdminID:
            kwargs = {
                'AdminID': AdminID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = AdministratorsController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, AdminID):
        if not AdminID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('AdminType', location='form', required=False, help='AdminType参数类型不正确或缺失')
        parser.add_argument('Account', location='form', required=False, help='Account参数类型不正确或缺失')
        parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
        parser.add_argument('Permissions', location='form', required=False, help='Permissions参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['AdminID'] = AdminID

        res = AdministratorsController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        AdministratorsList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('AdministratorsList', type=str, location='form', required=False, help='AdministratorsList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('AdministratorsList'):
            kwargs['AdministratorsList'] = json.loads(kwargs['AdministratorsList'])
            for data in kwargs['AdministratorsList']:
                for key in []:
                    data.pop(key, None)
            res = AdministratorsController.add_list(**kwargs)

        else:
            parser.add_argument('AdminID', location='form', required=True, help='AdminID参数类型不正确或缺失')
            parser.add_argument('AdminType', location='form', required=False, help='AdminType参数类型不正确或缺失')
            parser.add_argument('Account', location='form', required=False, help='Account参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
            parser.add_argument('Permissions', location='form', required=False, help='Permissions参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = AdministratorsController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
