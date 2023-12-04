#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.theaters import Theaters
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class TheatersController(Theaters):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Theaters(
                TheaterID=kwargs.get('TheaterID'),
                TheaterName=kwargs.get('TheaterName'),
                Address=kwargs.get('Address'),
                Capacity=kwargs.get('Capacity'),
                AdminID=kwargs.get('AdminID'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'TheaterID': model.TheaterID,
                
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
            if kwargs.get('TheaterID'):
                filter_list.append(cls.TheaterID == kwargs['TheaterID'])
            else:
                if kwargs.get('TheaterName'):
                    filter_list.append(cls.TheaterName == kwargs.get('TheaterName'))
                if kwargs.get('Address'):
                    filter_list.append(cls.Address == kwargs.get('Address'))
                if kwargs.get('Capacity') is not None:
                    filter_list.append(cls.Capacity == kwargs.get('Capacity'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            theaters_info = db.session.query(cls).filter(*filter_list)
            
            count = theaters_info.count()
            pages = math.ceil(count / size)
            theaters_info = theaters_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(theaters_info)
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
            if kwargs.get('TheaterID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('TheaterID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.TheaterID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('TheaterName'):
                    filter_list.append(cls.TheaterName == kwargs.get('TheaterName'))
                if kwargs.get('Address'):
                    filter_list.append(cls.Address == kwargs.get('Address'))
                if kwargs.get('Capacity') is not None:
                    filter_list.append(cls.Capacity == kwargs.get('Capacity'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'TheaterID': []
            }
            for query_model in res.all():
                results['TheaterID'].append(query_model.TheaterID)

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
            filter_list.append(cls.TheaterID == kwargs.get('TheaterID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'TheaterID': res.first().TheaterID,
                
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
        param_list = kwargs.get('TheatersList')
        model_list = []
        for param_dict in param_list:
            
            model = Theaters(
                TheaterID=param_dict.get('TheaterID'),
                TheaterName=param_dict.get('TheaterName'),
                Address=param_dict.get('Address'),
                Capacity=param_dict.get('Capacity'),
                AdminID=param_dict.get('AdminID'),
                
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
                added_record['TheaterID'] = model.TheaterID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
