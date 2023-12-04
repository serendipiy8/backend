#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.adminfunctionsController import AdminfunctionsController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class AdminfunctionsResource(Resource):

    # get
    @classmethod
    def get(cls, FunctionID=None):
        if FunctionID:
            kwargs = {
                'FunctionID': FunctionID
            }

            res = AdminfunctionsController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('FunctionID', location='args', required=False, help='FunctionID参数类型不正确或缺失')
        parser.add_argument('Name', location='args', required=False, help='Name参数类型不正确或缺失')
        parser.add_argument('Permissions', location='args', required=False, help='Permissions参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = AdminfunctionsController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, FunctionID=None):
        if FunctionID:
            kwargs = {
                'FunctionID': FunctionID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = AdminfunctionsController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, FunctionID):
        if not FunctionID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('Name', location='form', required=False, help='Name参数类型不正确或缺失')
        parser.add_argument('Permissions', location='form', required=False, help='Permissions参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['FunctionID'] = FunctionID

        res = AdminfunctionsController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        AdminfunctionsList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('AdminfunctionsList', type=str, location='form', required=False, help='AdminfunctionsList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('AdminfunctionsList'):
            kwargs['AdminfunctionsList'] = json.loads(kwargs['AdminfunctionsList'])
            for data in kwargs['AdminfunctionsList']:
                for key in []:
                    data.pop(key, None)
            res = AdminfunctionsController.add_list(**kwargs)

        else:
            parser.add_argument('FunctionID', location='form', required=True, help='FunctionID参数类型不正确或缺失')
            parser.add_argument('Name', location='form', required=False, help='Name参数类型不正确或缺失')
            parser.add_argument('Permissions', location='form', required=False, help='Permissions参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = AdminfunctionsController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
