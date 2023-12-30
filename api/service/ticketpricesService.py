#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.ticketpricesController import TicketpricesController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class TicketpricesService(TicketpricesController):

    @classmethod
    def ticketprices_query(cls, **kwargs):
        userid = kwargs.get('UserID')
        realname = kwargs.get('RealName')
        gender = kwargs.get('Gender')
        idcard = kwargs.get('IDcard')
        address = kwargs.get('Address')
        account = kwargs.get('Account')
        email = kwargs.get('Email')

        try:
            existing_user = db.session.query(cls).filter_by(UserID=userid).first()
            if existing_user == None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "用户id不存在"}

            existing_user.Gender = gender
            existing_user.RealName = realname
            existing_user.IDCard = idcard
            existing_user.Address = address
            existing_user.Account = account
            existing_user.Email = email

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RealName,
                cls.Gender,
            ).filter(cls.UserID == userid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RealName": user_info['RealName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
            pass


    @classmethod
    def ticketprices_post(cls, **kwargs):
        userid = kwargs.get('UserID')
        realname = kwargs.get('RealName')
        gender = kwargs.get('Gender')
        idcard = kwargs.get('IDcard')
        address = kwargs.get('Address')
        account = kwargs.get('Account')
        email = kwargs.get('Email')

        try:
            existing_user = db.session.query(cls).filter_by(UserID=userid).first()
            if existing_user == None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "用户id不存在"}

            existing_user.Gender = gender
            existing_user.RealName = realname
            existing_user.IDCard = idcard
            existing_user.Address = address
            existing_user.Account = account
            existing_user.Email = email

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RealName,
                cls.Gender,
            ).filter(cls.UserID == userid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RealName": user_info['RealName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
            pass


    @classmethod
    def ticketprices_put(cls, **kwargs):
        userid = kwargs.get('UserID')
        realname = kwargs.get('RealName')
        gender = kwargs.get('Gender')
        idcard = kwargs.get('IDcard')
        address = kwargs.get('Address')
        account = kwargs.get('Account')
        email = kwargs.get('Email')

        try:
            existing_user = db.session.query(cls).filter_by(UserID=userid).first()
            if existing_user == None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "用户id不存在"}

            existing_user.Gender = gender
            existing_user.RealName = realname
            existing_user.IDCard = idcard
            existing_user.Address = address
            existing_user.Account = account
            existing_user.Email = email

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RealName,
                cls.Gender,
            ).filter(cls.UserID == userid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RealName": user_info['RealName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
            pass


    @classmethod
    def ticketprices_del(cls, **kwargs):
        userid = kwargs.get('UserID')
        realname = kwargs.get('RealName')
        gender = kwargs.get('Gender')
        idcard = kwargs.get('IDcard')
        address = kwargs.get('Address')
        account = kwargs.get('Account')
        email = kwargs.get('Email')

        try:
            existing_user = db.session.query(cls).filter_by(UserID=userid).first()
            if existing_user == None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "用户id不存在"}

            existing_user.Gender = gender
            existing_user.RealName = realname
            existing_user.IDCard = idcard
            existing_user.Address = address
            existing_user.Account = account
            existing_user.Email = email

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RealName,
                cls.Gender,
            ).filter(cls.UserID == userid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RealName": user_info['RealName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
            pass