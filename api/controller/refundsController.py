#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.refunds import Refunds
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class RefundsController(Refunds):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Refunds(
                RefundID=kwargs.get('RefundID'),
                UserID=kwargs.get('UserID'),
                AdminID=kwargs.get('AdminID'),
                RefundTime=kwargs.get('RefundTime'),
                RefundReason=kwargs.get('RefundReason'),
                TicketStatus=kwargs.get('TicketStatus'),
                OrderID=kwargs.get('OrderID'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RefundID': model.RefundID,
                
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
            if kwargs.get('RefundID'):
                filter_list.append(cls.RefundID == kwargs['RefundID'])
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                if kwargs.get('RefundTime'):
                    filter_list.append(cls.RefundTime == kwargs.get('RefundTime'))
                if kwargs.get('RefundReason'):
                    filter_list.append(cls.RefundReason == kwargs.get('RefundReason'))
                if kwargs.get('TicketStatus'):
                    filter_list.append(cls.TicketStatus == kwargs.get('TicketStatus'))
                if kwargs.get('OrderID') is not None:
                    filter_list.append(cls.OrderID == kwargs.get('OrderID'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            refunds_info = db.session.query(cls).filter(*filter_list)
            
            count = refunds_info.count()
            pages = math.ceil(count / size)
            refunds_info = refunds_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(refunds_info)
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
            if kwargs.get('RefundID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('RefundID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.RefundID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                if kwargs.get('RefundTime'):
                    filter_list.append(cls.RefundTime == kwargs.get('RefundTime'))
                if kwargs.get('RefundReason'):
                    filter_list.append(cls.RefundReason == kwargs.get('RefundReason'))
                if kwargs.get('TicketStatus'):
                    filter_list.append(cls.TicketStatus == kwargs.get('TicketStatus'))
                if kwargs.get('OrderID') is not None:
                    filter_list.append(cls.OrderID == kwargs.get('OrderID'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RefundID': []
            }
            for query_model in res.all():
                results['RefundID'].append(query_model.RefundID)

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
            filter_list.append(cls.RefundID == kwargs.get('RefundID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'RefundID': res.first().RefundID,
                
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
        param_list = kwargs.get('RefundsList')
        model_list = []
        for param_dict in param_list:
            
            model = Refunds(
                RefundID=param_dict.get('RefundID'),
                UserID=param_dict.get('UserID'),
                AdminID=param_dict.get('AdminID'),
                RefundTime=param_dict.get('RefundTime'),
                RefundReason=param_dict.get('RefundReason'),
                TicketStatus=param_dict.get('TicketStatus'),
                OrderID=param_dict.get('OrderID'),
                
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
                added_record['RefundID'] = model.RefundID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
