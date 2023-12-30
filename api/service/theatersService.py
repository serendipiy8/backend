#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.theatersController import TheatersController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class TheatersService(TheatersController):

    @classmethod
    def theaters_post(cls, **kwargs):
        theatername = kwargs.get('TheaterName')
        address = kwargs.get('Address')
        capacity = kwargs.get('Capacity')
        adminid = kwargs.get('AdminID')

        try:
            existing_user = db.session.query(cls).filter_by(TheaterName=theatername).first()
            if existing_user:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "剧院已存在"}

            id = int(GenerateID.create_random_id())
            new_user = cls(TheaterID=id, TheaterName=theatername, Address=address,Capacity=capacity,AdminID=adminid)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.TheaterID,
                cls.TheaterName,
                cls.Address,
                cls.Capacity,
                cls.AdminID,
            ).filter(cls.TheaterName==theatername).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "theaterid": user_info['TheaterID'],
                "theatername": user_info['TheaterName'],
                "address": user_info['Address'],
                "capacity": user_info['Capacity'],
                "adminid": user_info['AdminID'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def theaters_query(cls, **kwargs):
        account = kwargs.get('account')
        password = kwargs.get('password')
        password_again = kwargs.get('password_again')

        try:
            if password != password_again:
                return {'code': RET.PWDERR, 'message': error_map_EN[RET.PWDERR], 'error': '两次输入密码不一致'}

            existing_user = db.session.query(cls).filter_by(Account=account).first()
            if existing_user:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "账户已存在"}

            id = int(GenerateID.create_random_id())
            new_user = cls(UserID=id, Account=account, Password=password)
            # new_user.add(Account=account, Password=password)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.Account,
                cls.Password,
            ).filter(cls.Account == account).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "account": user_info['Account'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def theaters_revise(cls, **kwargs):
        account = kwargs.get('account')
        password = kwargs.get('password')
        password_again = kwargs.get('password_again')

        try:
            if password != password_again:
                return {'code': RET.PWDERR, 'message': error_map_EN[RET.PWDERR], 'error': '两次输入密码不一致'}

            existing_user = db.session.query(cls).filter_by(Account=account).first()
            if existing_user:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "账户已存在"}

            id = int(GenerateID.create_random_id())
            new_user = cls(UserID=id, Account=account, Password=password)
            # new_user.add(Account=account, Password=password)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.Account,
                cls.Password,
            ).filter(cls.Account == account).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "account": user_info['Account'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def theaters_delete(cls, **kwargs):
        account = kwargs.get('account')
        password = kwargs.get('password')
        password_again = kwargs.get('password_again')

        try:
            if password != password_again:
                return {'code': RET.PWDERR, 'message': error_map_EN[RET.PWDERR], 'error': '两次输入密码不一致'}

            existing_user = db.session.query(cls).filter_by(Account=account).first()
            if existing_user:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "账户已存在"}

            id = int(GenerateID.create_random_id())
            new_user = cls(UserID=id, Account=account, Password=password)
            # new_user.add(Account=account, Password=password)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.Account,
                cls.Password,
            ).filter(cls.Account == account).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "account": user_info['Account'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
    pass
