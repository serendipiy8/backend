#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.shows import Shows
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class ShowsController(Shows):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Shows(
                ShowID=kwargs.get('ShowID'),
                TheaterID=kwargs.get('TheaterID'),
                ShowName=kwargs.get('ShowName'),
                Description=kwargs.get('Description'),
                ShowDate=kwargs.get('ShowDate'),
                Duration=kwargs.get('Duration'),
                AdminID=kwargs.get('AdminID'),
                Image=kwargs.get('Image'),
                Category=kwargs.get('Category'),
                City=kwargs.get('City'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ShowID': model.ShowID,
                
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
            if kwargs.get('ShowID'):
                filter_list.append(cls.ShowID == kwargs['ShowID'])
            else:
                if kwargs.get('TheaterID') is not None:
                    filter_list.append(cls.TheaterID == kwargs.get('TheaterID'))
                if kwargs.get('ShowName'):
                    filter_list.append(cls.ShowName == kwargs.get('ShowName'))
                if kwargs.get('Description'):
                    filter_list.append(cls.Description == kwargs.get('Description'))
                if kwargs.get('ShowDate'):
                    filter_list.append(cls.ShowDate == kwargs.get('ShowDate'))
                if kwargs.get('Duration') is not None:
                    filter_list.append(cls.Duration == kwargs.get('Duration'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                if kwargs.get('Image'):
                    filter_list.append(cls.Image == kwargs.get('Image'))
                if kwargs.get('Category'):
                    filter_list.append(cls.Category == kwargs.get('Category'))
                if kwargs.get('City'):
                    filter_list.append(cls.City == kwargs.get('City'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            shows_info = db.session.query(cls).filter(*filter_list)
            
            count = shows_info.count()
            pages = math.ceil(count / size)
            shows_info = shows_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(shows_info)
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
            if kwargs.get('ShowID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('ShowID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.ShowID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('TheaterID') is not None:
                    filter_list.append(cls.TheaterID == kwargs.get('TheaterID'))
                if kwargs.get('ShowName'):
                    filter_list.append(cls.ShowName == kwargs.get('ShowName'))
                if kwargs.get('Description'):
                    filter_list.append(cls.Description == kwargs.get('Description'))
                if kwargs.get('ShowDate'):
                    filter_list.append(cls.ShowDate == kwargs.get('ShowDate'))
                if kwargs.get('Duration') is not None:
                    filter_list.append(cls.Duration == kwargs.get('Duration'))
                if kwargs.get('AdminID') is not None:
                    filter_list.append(cls.AdminID == kwargs.get('AdminID'))
                if kwargs.get('Image'):
                    filter_list.append(cls.Image == kwargs.get('Image'))
                if kwargs.get('Category'):
                    filter_list.append(cls.Category == kwargs.get('Category'))
                if kwargs.get('City'):
                    filter_list.append(cls.City == kwargs.get('City'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'ShowID': []
            }
            for query_model in res.all():
                results['ShowID'].append(query_model.ShowID)

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
            filter_list.append(cls.ShowID == kwargs.get('ShowID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()
            if res.first():
                results = {
                    'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'ShowID': res.first().ShowID,
                
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
        param_list = kwargs.get('ShowsList')
        model_list = []
        for param_dict in param_list:
            
            model = Shows(
                ShowID=param_dict.get('ShowID'),
                TheaterID=param_dict.get('TheaterID'),
                ShowName=param_dict.get('ShowName'),
                Description=param_dict.get('Description'),
                ShowDate=param_dict.get('ShowDate'),
                Duration=param_dict.get('Duration'),
                AdminID=param_dict.get('AdminID'),
                Image=param_dict.get('Image'),
                Category=param_dict.get('Category'),
                City=param_dict.get('City'),
                
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
                added_record['ShowID'] = model.ShowID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
