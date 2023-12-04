#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.ticketpricesController import TicketpricesController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class TicketpricesResource(Resource):

    # get
    @classmethod
    def get(cls, TicketID=None):
        if TicketID:
            kwargs = {
                'TicketID': TicketID
            }

            res = TicketpricesController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('TicketID', location='args', required=False, help='TicketID参数类型不正确或缺失')
        parser.add_argument('ShowID', location='args', required=False, help='ShowID参数类型不正确或缺失')
        parser.add_argument('Price', location='args', required=False, help='Price参数类型不正确或缺失')
        parser.add_argument('Category', location='args', required=False, help='Category参数类型不正确或缺失')
        parser.add_argument('TotalQuantity', location='args', required=False, help='TotalQuantity参数类型不正确或缺失')
        parser.add_argument('RemainingQuantity', location='args', required=False, help='RemainingQuantity参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = TicketpricesController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, TicketID=None):
        if TicketID:
            kwargs = {
                'TicketID': TicketID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = TicketpricesController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, TicketID):
        if not TicketID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('ShowID', location='form', required=False, help='ShowID参数类型不正确或缺失')
        parser.add_argument('Price', location='form', required=False, help='Price参数类型不正确或缺失')
        parser.add_argument('Category', location='form', required=False, help='Category参数类型不正确或缺失')
        parser.add_argument('TotalQuantity', location='form', required=False, help='TotalQuantity参数类型不正确或缺失')
        parser.add_argument('RemainingQuantity', location='form', required=False, help='RemainingQuantity参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['TicketID'] = TicketID

        res = TicketpricesController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        TicketpricesList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('TicketpricesList', type=str, location='form', required=False, help='TicketpricesList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('TicketpricesList'):
            kwargs['TicketpricesList'] = json.loads(kwargs['TicketpricesList'])
            for data in kwargs['TicketpricesList']:
                for key in []:
                    data.pop(key, None)
            res = TicketpricesController.add_list(**kwargs)

        else:
            parser.add_argument('TicketID', location='form', required=True, help='TicketID参数类型不正确或缺失')
            parser.add_argument('ShowID', location='form', required=False, help='ShowID参数类型不正确或缺失')
            parser.add_argument('Price', location='form', required=False, help='Price参数类型不正确或缺失')
            parser.add_argument('Category', location='form', required=False, help='Category参数类型不正确或缺失')
            parser.add_argument('TotalQuantity', location='form', required=False, help='TotalQuantity参数类型不正确或缺失')
            parser.add_argument('RemainingQuantity', location='form', required=False, help='RemainingQuantity参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = TicketpricesController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
