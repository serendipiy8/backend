#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.theatersController import TheatersController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class TheatersResource(Resource):

    # get
    @classmethod
    def get(cls, TheaterID=None):
        if TheaterID:
            kwargs = {
                'TheaterID': TheaterID
            }

            res = TheatersController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('TheaterID', location='args', required=False, help='TheaterID参数类型不正确或缺失')
        parser.add_argument('TheaterName', location='args', required=False, help='TheaterName参数类型不正确或缺失')
        parser.add_argument('Address', location='args', required=False, help='Address参数类型不正确或缺失')
        parser.add_argument('Capacity', location='args', required=False, help='Capacity参数类型不正确或缺失')
        parser.add_argument('AdminID', location='args', required=False, help='AdminID参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = TheatersController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, TheaterID=None):
        if TheaterID:
            kwargs = {
                'TheaterID': TheaterID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = TheatersController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, TheaterID):
        if not TheaterID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('TheaterName', location='form', required=False, help='TheaterName参数类型不正确或缺失')
        parser.add_argument('Address', location='form', required=False, help='Address参数类型不正确或缺失')
        parser.add_argument('Capacity', location='form', required=False, help='Capacity参数类型不正确或缺失')
        parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['TheaterID'] = TheaterID

        res = TheatersController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        TheatersList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('TheatersList', type=str, location='form', required=False, help='TheatersList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('TheatersList'):
            kwargs['TheatersList'] = json.loads(kwargs['TheatersList'])
            for data in kwargs['TheatersList']:
                for key in []:
                    data.pop(key, None)
            res = TheatersController.add_list(**kwargs)

        else:
            parser.add_argument('TheaterID', location='form', required=True, help='TheaterID参数类型不正确或缺失')
            parser.add_argument('TheaterName', location='form', required=False, help='TheaterName参数类型不正确或缺失')
            parser.add_argument('Address', location='form', required=False, help='Address参数类型不正确或缺失')
            parser.add_argument('Capacity', location='form', required=False, help='Capacity参数类型不正确或缺失')
            parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = TheatersController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
