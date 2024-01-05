#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.administratorsController import AdministratorsController
from controller.administratorsController import AdministratorsController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class AdministratorsService(AdministratorsController):

    @classmethod
    def administrators_post(cls, **kwargs):
        admintype = kwargs.get('AdminType')
        account = kwargs.get('Account')
        password = kwargs.get('Password')
        permissions = kwargs.get('Permissions')

        try:

            id = int(GenerateID.create_random_id())
            new_administrotor = cls(AdminID=id, AdminType=admintype, Account=account, Password=password,
                           Permissions=permissions)
            db.session.add(new_administrotor)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.AdminID,
                cls.AdminType,
                cls.Account,
                cls.Password,
                cls.Permissions,
            ).filter(cls.AdminID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "AdminID": user_info['AdminID'],
                "AdminType": user_info['AdminType'],
                "Account": user_info['Account'],
                "Password": user_info['Password'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def administrators_query(cls, **kwargs):
        adminid = kwargs.get('AdminID')

        try:

            existing_order = db.session.query(cls).filter_by(AdminID=adminid).first()
            if existing_order is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入剧院ID"}

            # 获取新用户信息
            shows = db.session.query(
                cls.AdminID,
                cls.AdminType,
                cls.Account,
                cls.Password,
                cls.Permissions,
            ).filter(cls.AdminID == adminid)

            db.session.close()

            back_array = []
            for i in shows:
                user_info = i
                user_info = dict(user_info._asdict())

                back_element = {
                    "AdminID": user_info['AdminID'],
                    "AdminType": user_info['AdminType'],
                    "Account": user_info['Account'],
                    "Password": user_info['Password'],
                    "Permissions": user_info['Permissions'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def administrators_revise(cls, **kwargs):
        adminid = kwargs.get('AdminID')
        admintype = kwargs.get('AdminType')
        account = kwargs.get('Account')
        password = kwargs.get('Password')
        permissions = kwargs.get('Permissions')

        try:

            existing_administrator = db.session.query(cls).filter_by(AdminID=adminid).first()
            if existing_administrator is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "修改管理员不存在"}

            for attr_name in ['Account', 'Password', 'Permissions', 'AdminType']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_administrator, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.AdminID,
                cls.AdminType,
                cls.Account,
                cls.Password,
                cls.Permissions,
            ).filter(cls.AdminID == adminid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                 "AdminID": user_info['AdminID'],
                "AdminType": user_info['AdminType'],
                "Account": user_info['Account'],
                "Password": user_info['Password'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def administrators_delete(cls, **kwargs):
        adminid = kwargs.get('AdminID')

        try:

            existing_administrator = db.session.query(cls).filter_by(AdminID=adminid).first()
            if existing_administrator is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA],
                        'error': "想要删除的管理员ID不存在"}

            user_info = db.session.query(
                cls.AdminID,
                cls.AdminType,
                cls.Account,
                cls.Password,
                cls.Permissions,
            ).filter(cls.AdminID == adminid).first()

            db.session.delete(existing_administrator)
            db.session.commit()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "AdminID": user_info['AdminID'],
                "AdminType": user_info['AdminType'],
                "Account": user_info['Account'],
                "Password": user_info['Password'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
    
    pass
