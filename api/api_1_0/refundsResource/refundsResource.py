#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.refundsController import RefundsController
from utils import commons
from utils.response_code import RET, error_map_EN
import json


class RefundsResource(Resource):

    # get
    @classmethod
    def get(cls, RefundID=None):
        if RefundID:
            kwargs = {
                'RefundID': RefundID
            }

            res = RefundsController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('RefundID', location='args', required=False, help='RefundID参数类型不正确或缺失')
        parser.add_argument('UserID', location='args', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('AdminID', location='args', required=False, help='AdminID参数类型不正确或缺失')
        parser.add_argument('RefundTime', location='args', required=False, help='RefundTime参数类型不正确或缺失')
        parser.add_argument('RefundReason', location='args', required=False, help='RefundReason参数类型不正确或缺失')
        parser.add_argument('TicketStatus', location='args', required=False, help='TicketStatus参数类型不正确或缺失')
        parser.add_argument('OrderID', location='args', required=False, help='OrderID参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = RefundsController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, RefundID=None):
        if RefundID:
            kwargs = {
                'RefundID': RefundID
            }

        else:
            return jsonify(code=RET.PARAMERR, message=error_map_EN[RET.PARAMERR], data='id不能为空')

        res = RefundsController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, RefundID):
        if not RefundID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
        parser.add_argument('RefundTime', location='form', required=False, help='RefundTime参数类型不正确或缺失')
        parser.add_argument('RefundReason', location='form', required=False, help='RefundReason参数类型不正确或缺失')
        parser.add_argument('TicketStatus', location='form', required=False, help='TicketStatus参数类型不正确或缺失')
        parser.add_argument('OrderID', location='form', required=False, help='OrderID参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['RefundID'] = RefundID

        res = RefundsController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        RefundsList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('RefundsList', type=str, location='form', required=False, help='RefundsList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('RefundsList'):
            kwargs['RefundsList'] = json.loads(kwargs['RefundsList'])
            for data in kwargs['RefundsList']:
                for key in []:
                    data.pop(key, None)
            res = RefundsController.add_list(**kwargs)

        else:
            parser.add_argument('RefundID', location='form', required=True, help='RefundID参数类型不正确或缺失')
            parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
            parser.add_argument('AdminID', location='form', required=False, help='AdminID参数类型不正确或缺失')
            parser.add_argument('RefundTime', location='form', required=False, help='RefundTime参数类型不正确或缺失')
            parser.add_argument('RefundReason', location='form', required=False, help='RefundReason参数类型不正确或缺失')
            parser.add_argument('TicketStatus', location='form', required=False, help='TicketStatus参数类型不正确或缺失')
            parser.add_argument('OrderID', location='form', required=False, help='OrderID参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = RefundsController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
