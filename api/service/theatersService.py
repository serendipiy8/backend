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

        try:
            existing_show = db.session.query(cls).all()
            if existing_show==None:
                return {'code': RET.DATAERR, 'message': error_map_EN[RET.DATAERR], 'error': "查询数据不存在"}

            back_show=[]
            for entry in existing_show:
                show_dict={
                    'TheaterID':entry.TheaterID,
                    'TheaterName': entry.TheaterName,
                    'Address': entry.Address,
                    'Capacity': entry.Capacity,
                    'AdminID': entry.AdminID
                }
                back_show.append(show_dict)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_show}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def theaters_revise(cls, **kwargs):
        theaterid = kwargs.get('TheaterID')
        theatername = kwargs.get('TheaterName')
        address = kwargs.get('Address')
        capacity = kwargs.get('Capacity')

        try:

            existing_show = db.session.query(cls).filter_by(TheaterID=theaterid).first()
            if existing_show is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "修改演出不存在"}

            for attr_name in ['TheaterName', 'Address', 'Capacity']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_show, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.TheaterID,
                cls.TheaterName,
                cls.Address,
                cls.Capacity,
                cls.AdminID,
            ).filter(cls.TheaterID ==theaterid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "TheaterID": user_info['TheaterID'],
                "TheaterName": user_info['TheaterName'],
                "Address": user_info['Address'],
                "Capacity": user_info['Capacity'],
                "AdminID": user_info['AdminID'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def theaters_delete(cls, **kwargs):
        theaterid = kwargs.get('TheaterID')

        try:
            existing_theater = db.session.query(cls).filter_by(TheaterID=theaterid).first()
            if existing_theater == None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "数据不存在"}

            db.session.delete(existing_theater)
            db.session.commit()


            user_info = dict(existing_theater._asdict())

            db.session.close()

            back_dict = {
                'TheaterID': user_info["TheaterID"],
                'TheaterName': user_info["TheaterName"],
                'Address': user_info["Address"],
                'Capacity': user_info["Capacity"],
                'AdminID': user_info["AdminID"],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
    pass
