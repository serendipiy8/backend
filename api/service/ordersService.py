#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.ordersController import OrdersController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class OrdersService(OrdersController):
    @classmethod
    def orders_post(cls, **kwargs):
        userid = kwargs.get('UserID')
        ticketid = kwargs.get('TicketID')
        purchasetime = kwargs.get('PurchaseTime')
        orderstatus = kwargs.get('OrderStatus')
        quantity = kwargs.get('Quantity')

        try:

            id = int(GenerateID.create_random_id())
            new_order = cls(OrderID=id, UserID=userid, TicketID=ticketid, PurchaseTime=purchasetime,
                                    OrderStatus=orderstatus,Quantity=quantity)

            db.session.add(new_order)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.OrderID,
                cls.UserID,
                cls.TicketID,
                cls.PurchaseTime,
                cls.OrderStatus,
                cls.Quantity,
            ).filter(cls.OrderID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "OrderID": user_info['OrderID'],
                "UserID": user_info['UserID'],
                "TicketID": user_info['TicketID'],
                "PurchaseTime": user_info['PurchaseTime'],
                "OrderStatus": user_info['OrderStatus'],
                "Quantity": user_info['Quantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def orders_query(cls, **kwargs):
        orderid = kwargs.get('OrderID')

        try:

            existing_order= db.session.query(cls).filter_by(OrderID=orderid).first()
            if existing_order is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入订单ID"}

            # 获取新用户信息
            user_info = db.session.query(
                cls.OrderID,
                cls.UserID,
                cls.TicketID,
                cls.PurchaseTime,
                cls.OrderStatus,
                cls.Quantity,
            ).filter(cls.OrderID == orderid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "OrderID": user_info['OrderID'],
                "UserID": user_info['UserID'],
                "TicketID": user_info['TicketID'],
                "PurchaseTime": user_info['PurchaseTime'],
                "OrderStatus": user_info['OrderStatus'],
                "Quantity": user_info['Quantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def queryUser(cls, **kwargs):
        userid = kwargs.get('UserID')

        try:

            existing_order = db.session.query(cls).filter_by(UserID=userid).first()
            if existing_order is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入剧院ID"}

            # 获取新用户信息
            shows = db.session.query(
                cls.OrderID,
                cls.UserID,
                cls.TicketID,
                cls.PurchaseTime,
                cls.OrderStatus,
                cls.Quantity,
            ).filter(cls.UserID == userid)

            db.session.close()

            back_array = []
            for i in shows:
                user_info = i
                user_info = dict(user_info._asdict())

                back_element = {
                    "OrderID": user_info['OrderID'],
                    "UserID": user_info['UserID'],
                    "TicketID": user_info['TicketID'],
                    "PurchaseTime": user_info['PurchaseTime'],
                    "OrderStatus": user_info['OrderStatus'],
                    "Quantity": user_info['Quantity'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def orders_revise(cls, **kwargs):
        orderid = kwargs.get('OrderID')
        orderstatus = kwargs.get('OrderStatus')

        try:

            existing_show = db.session.query(cls).filter_by(OrderID=orderid).first()
            if existing_show is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "修改演出不存在"}

            for attr_name in ['OrderStatus']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_show, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.OrderID,
                cls.UserID,
                cls.TicketID,
                cls.PurchaseTime,
                cls.OrderStatus,
                cls.Quantity,
            ).filter(cls.OrderID == orderid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                    "OrderID": user_info['OrderID'],
                    "UserID": user_info['UserID'],
                    "TicketID": user_info['TicketID'],
                    "PurchaseTime": user_info['PurchaseTime'],
                    "OrderStatus": user_info['OrderStatus'],
                    "Quantity": user_info['Quantity'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    pass



    # @classmethod
    # def administrators_delete(cls, **kwargs):
    #     adminid = kwargs.get('AdminID')
    #
    #     try:
    #
    #         existing_administrator = db.session.query(cls).filter_by(AdminID=adminid).first()
    #         if existing_administrator is None:
    #             return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST],
    #                     'error': "想要删除的管理员ID不存在"}
    #
    #         user_info = db.session.query(
    #             cls.AdminID,
    #             cls.AdminType,
    #             cls.Account,
    #             cls.Password,
    #             cls.Permissions,
    #         ).filter(cls.AdminID == adminid).first()
    #
    #         db.session.delete(existing_administrator)
    #         db.session.commit()
    #
    #         user_info = dict(user_info._asdict())
    #
    #         db.session.close()
    #
    #         back_dict = {
    #             "AdminID": user_info['AdminID'],
    #             "AdminType": user_info['AdminType'],
    #             "Account": user_info['Account'],
    #             "Password": user_info['Password'],
    #             "Permissions": user_info['Permissions'],
    #         }
    #
    #         return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
    #     except Exception as e:
    #         loggings.exception(1, e)
    #         return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
    #     finally:
    #         db.session.close()
    #
    # pass
