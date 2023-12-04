#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.ticketprices import Ticketprices
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class TicketpricesController(Ticketprices):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Ticketprices(
                TicketID=kwargs.get('TicketID'),
                ShowID=kwargs.get('ShowID'),
                Price=kwargs.get('Price'),
                Category=kwargs.get('Category'),
                TotalQuantity=kwargs.get('TotalQuantity'),
                RemainingQuantity=kwargs.get('RemainingQuantity'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'TicketID': model.TicketID,
                
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
            if kwargs.get('TicketID'):
                filter_list.append(cls.TicketID == kwargs['TicketID'])
            else:
                if kwargs.get('ShowID') is not None:
                    filter_list.append(cls.ShowID == kwargs.get('ShowID'))
                if kwargs.get('Price'):
                    filter_list.append(cls.Price == kwargs.get('Price'))
                if kwargs.get('Category'):
                    filter_list.append(cls.Category == kwargs.get('Category'))
                if kwargs.get('TotalQuantity') is not None:
                    filter_list.append(cls.TotalQuantity == kwargs.get('TotalQuantity'))
                if kwargs.get('RemainingQuantity') is not None:
                    filter_list.append(cls.RemainingQuantity == kwargs.get('RemainingQuantity'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            ticketprices_info = db.session.query(cls).filter(*filter_list)
            
            count = ticketprices_info.count()
            pages = math.ceil(count / size)
            ticketprices_info = ticketprices_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(ticketprices_info)
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
            if kwargs.get('TicketID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('TicketID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.TicketID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('ShowID') is not None:
                    filter_list.append(cls.ShowID == kwargs.get('ShowID'))
                if kwargs.get('Price'):
                    filter_list.append(cls.Price == kwargs.get('Price'))
                if kwargs.get('Category'):
                    filter_list.append(cls.Category == kwargs.get('Category'))
                if kwargs.get('TotalQuantity') is not None:
                    filter_list.append(cls.TotalQuantity == kwargs.get('TotalQuantity'))
                if kwargs.get('RemainingQuantity') is not None:
                    filter_list.append(cls.RemainingQuantity == kwargs.get('RemainingQuantity'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'TicketID': []
            }
            for query_model in res.all():
                results['TicketID'].append(query_model.TicketID)

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
            filter_list.append(cls.TicketID == kwargs.get('TicketID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'TicketID': res.first().TicketID,
                
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
        param_list = kwargs.get('TicketpricesList')
        model_list = []
        for param_dict in param_list:
            
            model = Ticketprices(
                TicketID=param_dict.get('TicketID'),
                ShowID=param_dict.get('ShowID'),
                Price=param_dict.get('Price'),
                Category=param_dict.get('Category'),
                TotalQuantity=param_dict.get('TotalQuantity'),
                RemainingQuantity=param_dict.get('RemainingQuantity'),
                
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
                added_record['TicketID'] = model.TicketID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
