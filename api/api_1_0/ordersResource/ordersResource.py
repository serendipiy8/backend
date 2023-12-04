#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.ordersController import OrdersController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class OrdersResource(Resource):

    # get
    @classmethod
    def get(cls, OrderID=None):
        if OrderID:
            kwargs = {
                'OrderID': OrderID
            }

            res = OrdersController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('OrderID', location='args', required=False, help='OrderID参数类型不正确或缺失')
        parser.add_argument('UserID', location='args', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('TicketID', location='args', required=False, help='TicketID参数类型不正确或缺失')
        parser.add_argument('PurchaseTime', location='args', required=False, help='PurchaseTime参数类型不正确或缺失')
        parser.add_argument('OrderStatus', location='args', required=False, help='OrderStatus参数类型不正确或缺失')
        parser.add_argument('Quantity', location='args', required=False, help='Quantity参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = OrdersController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, OrderID=None):
        if OrderID:
            kwargs = {
                'OrderID': OrderID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = OrdersController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, OrderID):
        if not OrderID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('TicketID', location='form', required=False, help='TicketID参数类型不正确或缺失')
        parser.add_argument('PurchaseTime', location='form', required=False, help='PurchaseTime参数类型不正确或缺失')
        parser.add_argument('OrderStatus', location='form', required=False, help='OrderStatus参数类型不正确或缺失')
        parser.add_argument('Quantity', location='form', required=False, help='Quantity参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['OrderID'] = OrderID

        res = OrdersController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        OrdersList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('OrdersList', type=str, location='form', required=False, help='OrdersList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('OrdersList'):
            kwargs['OrdersList'] = json.loads(kwargs['OrdersList'])
            for data in kwargs['OrdersList']:
                for key in []:
                    data.pop(key, None)
            res = OrdersController.add_list(**kwargs)

        else:
            parser.add_argument('OrderID', location='form', required=True, help='OrderID参数类型不正确或缺失')
            parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
            parser.add_argument('TicketID', location='form', required=False, help='TicketID参数类型不正确或缺失')
            parser.add_argument('PurchaseTime', location='form', required=False, help='PurchaseTime参数类型不正确或缺失')
            parser.add_argument('OrderStatus', location='form', required=False, help='OrderStatus参数类型不正确或缺失')
            parser.add_argument('Quantity', location='form', required=False, help='Quantity参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = OrdersController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
