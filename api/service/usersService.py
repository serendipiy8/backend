#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET, error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from controller.usersController import UsersController
from dataclasses import asdict
from utils.generate_id import GenerateID


class UsersService(UsersController):

    @classmethod
    def login(cls, **kwargs):

        username = kwargs.get('username')
        password = kwargs.get('password')

        try:
            user_info = db.session.query(
                cls.UserName,
                cls.Password,
            ) \
                .filter(cls.UserName == username) \
                .first()

            if not user_info:
                return {'code': RET.LOGINERR, 'message': error_map_EN[RET.LOGINERR], 'error': "用户或密码错误"}

            user_info = dict(user_info._asdict())

            if not user_info['Password'] == password:
                return {'code': RET.LOGINERR, 'message': error_map_EN[RET.LOGINERR], 'error': "用户或密码错误"}

            db.session.close()

            print(user_info)
            back_dict = {
                "username": user_info['UserName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def register(cls, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        configurePassword = kwargs.get('configurePassword')

        try:
            if password != configurePassword:
                return {'code': RET.PWDERR, 'message': error_map_EN[RET.PWDERR], 'error': '两次输入密码不一致'}

            existing_user = db.session.query(cls).filter_by(UserName=username).first()
            if existing_user:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "账户已存在"}

            id = int(GenerateID.create_random_id())
            new_user = cls(UserID=id, Email=email, UserName=username, Password=password)
            # new_user.add(Account=account, Password=password)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.Email,
                cls.UserName,
                cls.Password,
            ).filter(cls.UserName == username).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "email": user_info['Email'],
                "username": user_info['UserName'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
