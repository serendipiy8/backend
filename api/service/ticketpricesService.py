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
    def ticketprices_post(cls, **kwargs):
        showid = kwargs.get('ShowID')
        price = kwargs.get('Price')
        category = kwargs.get('Category')
        totalquantity = kwargs.get('TotalQuantity')
        remainingquantity = kwargs.get('RemainingQuantity')

        try:

            id = int(GenerateID.create_random_id())
            new_administrotor = cls(TicketID=id, ShowID=showid, Price=price, Category=category,
                                    TotalQuantity=totalquantity,RemainingQuantity=remainingquantity)
            db.session.add(new_administrotor)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.TicketID,
                cls.ShowID,
                cls.Price,
                cls.Category,
                cls.TotalQuantity,
                cls.RemainingQuantity,
            ).filter(cls.TicketID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "TicketID": user_info['TicketID'],
                "ShowID": user_info['ShowID'],
                "Price": user_info['Price'],
                "Category": user_info['Category'],
                "TotalQuantity": user_info['TotalQuantity'],
                "RemainingQuantity": user_info['RemainingQuantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def ticketpricesQuery(cls, **kwargs):
        showid = kwargs.get('ShowID')

        try:

            existing_order = db.session.query(cls).filter_by(ShowID=showid).first()
            if existing_order is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入剧院ID"}

            # 获取新用户信息
            shows = db.session.query(
                cls.TicketID,
                cls.ShowID,
                cls.Price,
                cls.Category,
                cls.TotalQuantity,
                cls.RemainingQuantity,
            ).filter(cls.ShowID == showid)

            db.session.close()

            back_array = []
            for i in shows:
                user_info = i
                user_info = dict(user_info._asdict())

                back_element = {
                    "TicketID": user_info['TicketID'],
                    "ShowID": user_info['ShowID'],
                    "Price": user_info['Price'],
                    "Category": user_info['Category'],
                    "TotalQuantity": user_info['TotalQuantity'],
                    "RemainingQuantity": user_info['RemainingQuantity'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def ticketprices_revise(cls, **kwargs):
        ticketid = kwargs.get('TicketID')
        showid = kwargs.get('ShowID')
        price = kwargs.get('Price')
        category = kwargs.get('Category')
        totalquantity = kwargs.get('TotalQuantity')
        remainingquantity = kwargs.get('RemainingQuantity')

        try:

            existing_administrator = db.session.query(cls).filter_by(TicketID=ticketid).first()
            if existing_administrator is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "票ID不存在"}

            for attr_name in ['ShowID', 'Price', 'Category', 'TotalQuantity','RemainingQuantity']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_administrator, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.TicketID,
                cls.ShowID,
                cls.Price,
                cls.Category,
                cls.TotalQuantity,
                cls.RemainingQuantity,
            ).filter(cls.TicketID == ticketid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "TicketID": user_info['TicketID'],
                "ShowID": user_info['ShowID'],
                "Price": user_info['Price'],
                "Category": user_info['Category'],
                "TotalQuantity": user_info['TotalQuantity'],
                "RemainingQuantity": user_info['RemainingQuantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def ticketprices_delete(cls, **kwargs):
        ticketid = kwargs.get('TicketID')

        try:

            existing_administrator = db.session.query(cls).filter_by(TicketID=ticketid).first()
            if existing_administrator is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA],
                        'error': "想要删除的管理员ID不存在"}

            user_info = db.session.query(
                cls.TicketID,
                cls.ShowID,
                cls.Price,
                cls.Category,
                cls.TotalQuantity,
                cls.RemainingQuantity,
            ).filter(cls.TicketID == ticketid).first()

            db.session.delete(existing_administrator)
            db.session.commit()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "TicketID": user_info['TicketID'],
                "ShowID": user_info['ShowID'],
                "Price": user_info['Price'],
                "Category": user_info['Category'],
                "TotalQuantity": user_info['TotalQuantity'],
                "RemainingQuantity": user_info['RemainingQuantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    pass