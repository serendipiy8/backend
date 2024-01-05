#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.refundsController import RefundsController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class RefundsService(RefundsController):

    @classmethod
    def refunds_post(cls, **kwargs):
        userid = kwargs.get('UserID')
        adminid= kwargs.get('AdminID')
        refundtime = kwargs.get('RefundTime')
        refundreason = kwargs.get('RefundReason')
        ticketstatus = kwargs.get('TicketStatus')
        orderid = kwargs.get('OrderID')

        try:

            id = int(GenerateID.create_random_id())
            new_order = cls(RefundID=id, UserID=userid, AdminID=adminid, RefundTime=refundtime,
                            RefundReason=refundreason, TicketStatus=ticketstatus,OrderID=orderid)

            db.session.add(new_order)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RefundID,
                cls.UserID,
                cls.AdminID,
                cls.RefundTime,
                cls.RefundReason,
                cls.TicketStatus,
                cls.OrderID,
            ).filter(cls.RefundID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RefundID": user_info['RefundID'],
                "UserID": user_info['UserID'],
                "AdminID": user_info['AdminID'],
                "RefundTime": user_info['RefundTime'],
                "RefundReason": user_info['RefundReason'],
                "TicketStatus": user_info['TicketStatus'],
                "OrderID": user_info['OrderID'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def refundsOrder(cls, **kwargs):
        orderid = kwargs.get('OrderID')

        try:

            existing_order = db.session.query(cls).filter_by(OrderID=orderid).first()
            if existing_order is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入订单ID"}

            # 获取新用户信息
            shows = db.session.query(
                cls.RefundID,
                cls.UserID,
                cls.AdminID,
                cls.RefundTime,
                cls.RefundReason,
                cls.TicketStatus,
                cls.OrderID,
            ).filter(cls.OrderID == orderid)

            db.session.close()

            back_array = []
            for i in shows:
                user_info = i
                user_info = dict(user_info._asdict())

                back_element = {
                    "RefundID": user_info['RefundID'],
                    "UserID": user_info['UserID'],
                    "AdminID": user_info['AdminID'],
                    "RefundTime": user_info['RefundTime'],
                    "RefundReason": user_info['RefundReason'],
                    "TicketStatus": user_info['TicketStatus'],
                    "OrderID": user_info['OrderID'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def refunds_query(cls, **kwargs):
        refundid = kwargs.get('RefundID')

        try:
            existing_user = db.session.query(cls).filter_by(RefundID=refundid).first()
            if existing_user == None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "用户id不存在"}

            # 获取新用户信息
            user_info = db.session.query(
                cls.RefundID,
                cls.UserID,
                cls.AdminID,
                cls.RefundTime,
                cls.RefundReason,
                cls.TicketStatus,
                cls.OrderID,
            ).filter(cls.RefundID == refundid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RefundID": user_info['RefundID'],
                "UserID": user_info['UserID'],
                "AdminID": user_info['AdminID'],
                "RefundTime": user_info['RefundTime'],
                "RefundReason": user_info['RefundReason'],
                "TicketStatus": user_info['TicketStatus'],
                "OrderID": user_info['OrderID'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    @classmethod
    def refunds_revise(cls, **kwargs):
        refundid = kwargs.get('RefundID')
        ticketstatus = kwargs.get('TicketStatus')

        try:

            existing_show = db.session.query(cls).filter_by(RefundID=refundid).first()
            if existing_show is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "修改演出不存在"}

            for attr_name in ['TicketStatus']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_show, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.RefundID,
                cls.UserID,
                cls.AdminID,
                cls.RefundTime,
                cls.RefundReason,
                cls.TicketStatus,
                cls.OrderID,
            ).filter(cls.RefundID == refundid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "RefundID": user_info['RefundID'],
                "UserID": user_info['UserID'],
                "AdminID": user_info['AdminID'],
                "RefundTime": user_info['RefundTime'],
                "RefundReason": user_info['RefundReason'],
                "TicketStatus": user_info['TicketStatus'],
                "OrderID": user_info['OrderID'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()

    pass
