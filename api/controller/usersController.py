#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.users import Users
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class UsersController(Users):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Users(
                UserID=kwargs.get('UserID'),
                UserName=kwargs.get('UserName'),
                RealName=kwargs.get('RealName'),
                Gender=kwargs.get('Gender'),
                IDCard=kwargs.get('IDCard'),
                Email=kwargs.get('Email'),
                Address=kwargs.get('Address'),
                Account=kwargs.get('Account'),
                Password=kwargs.get('Password'),

            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'UserID': model.UserID,
                
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
            if kwargs.get('UserID'):
                filter_list.append(cls.UserID == kwargs['UserID'])
            else:
                if kwargs.get('UserName'):
                    filter_list.append(cls.UserName == kwargs.get('UserName'))
                if kwargs.get('RealName'):
                    filter_list.append(cls.RealName == kwargs.get('RealName'))
                if kwargs.get('Gender'):
                    filter_list.append(cls.Gender == kwargs.get('Gender'))
                if kwargs.get('IDCard'):
                    filter_list.append(cls.IDCard == kwargs.get('IDCard'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('Address'):
                    filter_list.append(cls.Address == kwargs.get('Address'))
                if kwargs.get('Account'):
                    filter_list.append(cls.Account == kwargs.get('Account'))
                if kwargs.get('Password'):
                    filter_list.append(cls.Password == kwargs.get('Password'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            users_info = db.session.query(cls).filter(*filter_list)
            
            count = users_info.count()
            pages = math.ceil(count / size)
            users_info = users_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(users_info)
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
            if kwargs.get('UserID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('UserID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.UserID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('UserName'):
                    filter_list.append(cls.UserName == kwargs.get('UserName'))
                if kwargs.get('RealName'):
                    filter_list.append(cls.RealName == kwargs.get('RealName'))
                if kwargs.get('Gender'):
                    filter_list.append(cls.Gender == kwargs.get('Gender'))
                if kwargs.get('IDCard'):
                    filter_list.append(cls.IDCard == kwargs.get('IDCard'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('Address'):
                    filter_list.append(cls.Address == kwargs.get('Address'))
                if kwargs.get('Account'):
                    filter_list.append(cls.Account == kwargs.get('Account'))
                if kwargs.get('Password'):
                    filter_list.append(cls.Password == kwargs.get('Password'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'UserID': []
            }
            for query_model in res.all():
                results['UserID'].append(query_model.UserID)

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
            filter_list.append(cls.UserID == kwargs.get('UserID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'UserID': res.first().UserID,
                
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
        param_list = kwargs.get('UsersList')
        model_list = []
        for param_dict in param_list:
            
            model = Users(
                UserID=param_dict.get('UserID'),
                UserName=param_dict.get('UserName'),
                RealName=param_dict.get('RealName'),
                Gender=param_dict.get('Gender'),
                IDCard=param_dict.get('IDCard'),
                Email=param_dict.get('Email'),
                Address=param_dict.get('Address'),
                Account=param_dict.get('Account'),
                Password=param_dict.get('Password'),
                
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
                added_record['UserID'] = model.UserID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
