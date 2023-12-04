#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.orders import Orders
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class OrdersController(Orders):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Orders(
                OrderID=kwargs.get('OrderID'),
                UserID=kwargs.get('UserID'),
                TicketID=kwargs.get('TicketID'),
                PurchaseTime=kwargs.get('PurchaseTime'),
                OrderStatus=kwargs.get('OrderStatus'),
                Quantity=kwargs.get('Quantity'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'OrderID': model.OrderID,
                
            }
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # get
    @classmethod
    def get(cls, **kwargs):
        try:
            filter_list = []
            if kwargs.get('OrderID'):
                filter_list.append(cls.OrderID == kwargs['OrderID'])
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('TicketID') is not None:
                    filter_list.append(cls.TicketID == kwargs.get('TicketID'))
                if kwargs.get('PurchaseTime'):
                    filter_list.append(cls.PurchaseTime == kwargs.get('PurchaseTime'))
                if kwargs.get('OrderStatus'):
                    filter_list.append(cls.OrderStatus == kwargs.get('OrderStatus'))
                if kwargs.get('Quantity') is not None:
                    filter_list.append(cls.Quantity == kwargs.get('Quantity'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            orders_info = db.session.query(cls).filter(*filter_list)
            
            count = orders_info.count()
            pages = math.ceil(count / size)
            orders_info = orders_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(orders_info)
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'totalPage': pages, 'data': results}
            
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # delete
    @classmethod
    def delete(cls, **kwargs):
        try:
            filter_list = []
            if kwargs.get('OrderID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('OrderID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.OrderID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('TicketID') is not None:
                    filter_list.append(cls.TicketID == kwargs.get('TicketID'))
                if kwargs.get('PurchaseTime'):
                    filter_list.append(cls.PurchaseTime == kwargs.get('PurchaseTime'))
                if kwargs.get('OrderStatus'):
                    filter_list.append(cls.OrderStatus == kwargs.get('OrderStatus'))
                if kwargs.get('Quantity') is not None:
                    filter_list.append(cls.Quantity == kwargs.get('Quantity'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'OrderID': []
            }
            for query_model in res.all():
                results['OrderID'].append(query_model.OrderID)

            res.delete()
            db.session.commit()

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # update
    @classmethod
    def update(cls, **kwargs):
        try:
            
            
            filter_list = []
            filter_list.append(cls.OrderID == kwargs.get('OrderID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'OrderID': res.first().OrderID,
                
                }
                
                res.update(kwargs)
                db.session.commit()
            else:
                results = {
                    'error': 'data dose not exist'
                }
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # batch add
    @classmethod
    def add_list(cls, **kwargs):
        param_list = kwargs.get('OrdersList')
        model_list = []
        for param_dict in param_list:
            
            model = Orders(
                OrderID=param_dict.get('OrderID'),
                UserID=param_dict.get('UserID'),
                TicketID=param_dict.get('TicketID'),
                PurchaseTime=param_dict.get('PurchaseTime'),
                OrderStatus=param_dict.get('OrderStatus'),
                Quantity=param_dict.get('Quantity'),
                
            )
            model_list.append(model)
        
        try:
            db.session.add_all(model_list)
            db.session.commit()
            results = {
                'added_records': [],
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for model in model_list:
                added_record = {}
                added_record['OrderID'] = model.OrderID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
