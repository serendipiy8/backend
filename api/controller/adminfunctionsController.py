#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.adminfunctions import Adminfunctions
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class AdminfunctionsController(Adminfunctions):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Adminfunctions(
                FunctionID=kwargs.get('FunctionID'),
                Name=kwargs.get('Name'),
                Permissions=kwargs.get('Permissions'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'FunctionID': model.FunctionID,
                
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
            if kwargs.get('FunctionID'):
                filter_list.append(cls.FunctionID == kwargs['FunctionID'])
            else:
                if kwargs.get('Name'):
                    filter_list.append(cls.Name == kwargs.get('Name'))
                if kwargs.get('Permissions'):
                    filter_list.append(cls.Permissions == kwargs.get('Permissions'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            adminfunctions_info = db.session.query(cls).filter(*filter_list)
            
            count = adminfunctions_info.count()
            pages = math.ceil(count / size)
            adminfunctions_info = adminfunctions_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(adminfunctions_info)
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
            if kwargs.get('FunctionID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('FunctionID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.FunctionID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('Name'):
                    filter_list.append(cls.Name == kwargs.get('Name'))
                if kwargs.get('Permissions'):
                    filter_list.append(cls.Permissions == kwargs.get('Permissions'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'FunctionID': []
            }
            for query_model in res.all():
                results['FunctionID'].append(query_model.FunctionID)

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
            filter_list.append(cls.FunctionID == kwargs.get('FunctionID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'FunctionID': res.first().FunctionID,
                
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
        param_list = kwargs.get('AdminfunctionsList')
        model_list = []
        for param_dict in param_list:
            
            model = Adminfunctions(
                FunctionID=param_dict.get('FunctionID'),
                Name=param_dict.get('Name'),
                Permissions=param_dict.get('Permissions'),
                
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
                added_record['FunctionID'] = model.FunctionID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
