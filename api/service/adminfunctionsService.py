#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.adminfunctionsController import AdminfunctionsController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class AdminfunctionsService(AdminfunctionsController):

    @classmethod
    def adminfunctions_post(cls, **kwargs):
        name = kwargs.get('Name')
        permissions = kwargs.get('Permissions')

        try:

            id = int(GenerateID.create_random_id())
            new_administrotor = cls(FunctionID=id, Name=name, Permissions=permissions)

            db.session.add(new_administrotor)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.FunctionID,
                cls.Name,
                cls.Permissions,
            ).filter(cls.FunctionID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "FunctionID": user_info['FunctionID'],
                "Name": user_info['Name'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def adminfunctions_revise(cls, **kwargs):
        functionid = kwargs.get('FunctionID')
        name = kwargs.get('Name')
        permissions = kwargs.get('Permissions')

        try:

            existing_administrator = db.session.query(cls).filter_by(FunctionID=functionid).first()
            if existing_administrator is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "功能不存在"}

            for attr_name in ['Name', 'Permissions']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_administrator, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.FunctionID,
                cls.Name,
                cls.Permissions,
            ).filter(cls.FunctionID == functionid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "FunctionID": user_info['FunctionID'],
                "Name": user_info['Name'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def adminfunctions_delete(cls, **kwargs):
        functionid = kwargs.get('FunctionID')

        try:

            existing_user = db.session.query(cls).filter_by(FunctionID=functionid).first()
            if existing_user is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA],
                        'error': "想要删除的演出ID不存在"}

            user_info = db.session.query(
                cls.FunctionID,
                cls.Name,
                cls.Permissions,
            ).filter(cls.FunctionID == functionid).first()

            db.session.delete(existing_user)
            db.session.commit()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "FunctionID": user_info['FunctionID'],
                "Name": user_info['Name'],
                "Permissions": user_info['Permissions'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    pass
