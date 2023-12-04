#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.showsController import ShowsController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class ShowsResource(Resource):

    # get
    @classmethod
    def get(cls, ShowID=None):
        if ShowID:
            kwargs = {
                'ShowID': ShowID
            }

            res = ShowsController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('ShowID', location='args', required=False, help='ShowID参数类型不正确或缺失')
        parser.add_argument('TheaterID', location='args', required=False, help='TheaterID参数类型不正确或缺失')
        parser.add_argument('ShowName', location='args', required=False, help='ShowName参数类型不正确或缺失')
        parser.add_argument('Description', location='args', required=False, help='Description参数类型不正确或缺失')
        parser.add_argument('ShowDate', location='args', required=False, help='ShowDate参数类型不正确或缺失')
        parser.add_argument('Duration', location='args', required=False, help='Duration参数类型不正确或缺失')
        parser.add_argument('AdminID', location='args', required=False, help='AdminID参数类型不正确或缺失')
        parser.add_argument('Image', location='args', required=False, help='Image参数类型不正确或缺失')
        parser.add_argument('Category', location='args', required=False, help='Category参数类型不正确或缺失')
        parser.add_argument('City', location='args', required=False, help='City参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = ShowsController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, ShowID=None):
        if ShowID:
            kwargs = {
                'ShowID': ShowID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = ShowsController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, ShowID):
        if not ShowID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('TheaterID', location='form', required=False, help='TheaterID参数类型不正确或缺失')
        parser.add_argument('ShowName', location='form', required=False, help='ShowName参数类型不正确或缺失')
        parser.add_argument('Description', location='form', required=False, help='Description参数类型不正确或缺失')
        parser.add_argument('ShowDate', location='form', required=False, help='ShowDate参数类型不正确或缺失')
        parser.add_argument('Duration', location='form', required=False, help='Duration参数类型不正确或缺失')
        parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
        parser.add_argument('Image', location='form', required=False, help='Image参数类型不正确或缺失')
        parser.add_argument('Category', location='form', required=False, help='Category参数类型不正确或缺失')
        parser.add_argument('City', location='form', required=False, help='City参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['ShowID'] = ShowID

        res = ShowsController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        ShowsList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('ShowsList', type=str, location='form', required=False, help='ShowsList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('ShowsList'):
            kwargs['ShowsList'] = json.loads(kwargs['ShowsList'])
            for data in kwargs['ShowsList']:
                for key in []:
                    data.pop(key, None)
            res = ShowsController.add_list(**kwargs)

        else:
            parser.add_argument('ShowID', location='form', required=True, help='ShowID参数类型不正确或缺失')
            parser.add_argument('TheaterID', location='form', required=False, help='TheaterID参数类型不正确或缺失')
            parser.add_argument('ShowName', location='form', required=False, help='ShowName参数类型不正确或缺失')
            parser.add_argument('Description', location='form', required=False, help='Description参数类型不正确或缺失')
            parser.add_argument('ShowDate', location='form', required=False, help='ShowDate参数类型不正确或缺失')
            parser.add_argument('Duration', location='form', required=False, help='Duration参数类型不正确或缺失')
            parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
            parser.add_argument('Image', location='form', required=False, help='Image参数类型不正确或缺失')
            parser.add_argument('Category', location='form', required=False, help='Category参数类型不正确或缺失')
            parser.add_argument('City', location='form', required=False, help='City参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = ShowsController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
