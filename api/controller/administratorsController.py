#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.administrators import Administrators
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class AdministratorsController(Administrators):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Administrators(
                AdminID=kwargs.get('AdminID'),
                AdminType=kwargs.get('AdminType'),
                Account=kwargs.get('Account'),
                Password=kwargs.get('Password'),
                Permissions=kwargs.get('Permissions'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'AdminID': model.AdminID,
                
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
            if kwargs.get('AdminID'):
                filter_list.append(cls.AdminID == kwargs['AdminID'])
            else:
                if kwargs.get('AdminType'):
                    filter_list.append(cls.AdminType == kwargs.get('AdminType'))
                if kwargs.get('Account'):
                    filter_list.append(cls.Account == kwargs.get('Account'))
                if kwargs.get('Password'):
                    filter_list.append(cls.Password == kwargs.get('Password'))
                if kwargs.get('Permissions'):
                    filter_list.append(cls.Permissions == kwargs.get('Permissions'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            administrators_info = db.session.query(cls).filter(*filter_list)
            
            count = administrators_info.count()
            pages = math.ceil(count / size)
            administrators_info = administrators_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(administrators_info)
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
            if kwargs.get('AdminID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('AdminID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.AdminID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('AdminType'):
                    filter_list.append(cls.AdminType == kwargs.get('AdminType'))
                if kwargs.get('Account'):
                    filter_list.append(cls.Account == kwargs.get('Account'))
                if kwargs.get('Password'):
                    filter_list.append(cls.Password == kwargs.get('Password'))
                if kwargs.get('Permissions'):
                    filter_list.append(cls.Permissions == kwargs.get('Permissions'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'AdminID': []
            }
            for query_model in res.all():
                results['AdminID'].append(query_model.AdminID)

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
            filter_list.append(cls.AdminID == kwargs.get('AdminID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'AdminID': res.first().AdminID,
                
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
        param_list = kwargs.get('AdministratorsList')
        model_list = []
        for param_dict in param_list:
            
            model = Administrators(
                AdminID=param_dict.get('AdminID'),
                AdminType=param_dict.get('AdminType'),
                Account=param_dict.get('Account'),
                Password=param_dict.get('Password'),
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
                added_record['AdminID'] = model.AdminID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
