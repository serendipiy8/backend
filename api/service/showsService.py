#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.showsController import ShowsController
from app import db
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET,error_map_EN
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from dataclasses import asdict
from utils.generate_id import GenerateID


class ShowsService(ShowsController):


    @classmethod
    def adminpost(cls, **kwargs):
        theaterid= kwargs.get('TheaterID')
        showname = kwargs.get('ShowName')
        description = kwargs.get('Description')
        showdate = kwargs.get('ShowDate')
        duration = kwargs.get('Duration')
        adminid = kwargs.get('AdminID')
        image = kwargs.get('Image')
        category = kwargs.get('Category')
        city=kwargs.get('City')

        try:

            id=int(GenerateID.create_random_id())
            new_user = cls(ShowID=id,TheaterID=theaterid,ShowName=showname,Description=description,ShowDate=showdate,Duration=duration,AdminID=adminid,Image=image,Category=category,City=city)
            db.session.add(new_user)
            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.ShowID == id).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "ShowID": user_info['ShowID'],
                "TheaterID": user_info['TheaterID'],
                "ShowName": user_info['ShowName'],
                "Description": user_info['Description'],
                "ShowDate": user_info['ShowDate'],
                "Duration": user_info['Duration'],
                "AdminID": user_info['AdminID'],
                "Image": user_info['Image'],
                "Category": user_info['Category'],
                "City": user_info['City'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()


    @classmethod
    def queryShowID(cls, **kwargs):
        showid = kwargs.get('ShowID')

        try:

            existing_show= db.session.query(cls).filter_by(ShowID=showid).first()
            if existing_show is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "查询不到输入演出ID"}

            # 获取新用户信息
            user_info = db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.ShowID == showid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                "ShowID": user_info['ShowID'],
                "TheaterID": user_info['TheaterID'],
                "ShowName": user_info['ShowName'],
                "Description": user_info['Description'],
                "ShowDate": user_info['ShowDate'],
                "Duration": user_info['Duration'],
                "AdminID": user_info['AdminID'],
                "Image": user_info['Image'],
                "Category": user_info['Category'],
                "City": user_info['City'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()


    @classmethod
    def queryShowName(cls, **kwargs):
        showname = kwargs.get('ShowName')

        try:

            existing_show = db.session.query(cls).filter_by(ShowName=showname).first()
            if existing_show is None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "查询不到输入演出名字"}

            # 获取新用户信息
            shows=db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.ShowName==showname)

            db.session.close()

            back_array=[]
            for i in shows:
                user_info=i
                user_info = dict(user_info._asdict())

                back_element = {
                "ShowID": user_info['ShowID'],
                "TheaterID": user_info['TheaterID'],
                "ShowName": user_info['ShowName'],
                "Description": user_info['Description'],
                "ShowDate": user_info['ShowDate'],
                "Duration": user_info['Duration'],
                "AdminID": user_info['AdminID'],
                "Image": user_info['Image'],
                "Category": user_info['Category'],
                "City": user_info['City'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()


    @classmethod
    def queryTheaterID(cls, **kwargs):
        theaterid = kwargs.get('TheaterID')

        try:

            existing_show = db.session.query(cls).filter_by(TheaterID = theaterid).first()
            if existing_show is None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "查询不到输入剧院ID"}

            # 获取新用户信息
            shows = db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.TheaterID == theaterid)

            db.session.close()

            back_array = []
            for i in shows:
                user_info = i
                user_info = dict(user_info._asdict())

                back_element = {
                    "ShowID": user_info['ShowID'],
                    "TheaterID": user_info['TheaterID'],
                    "ShowName": user_info['ShowName'],
                    "Description": user_info['Description'],
                    "ShowDate": user_info['ShowDate'],
                    "Duration": user_info['Duration'],
                    "AdminID": user_info['AdminID'],
                    "Image": user_info['Image'],
                    "Category": user_info['Category'],
                    "City": user_info['City'],
                }
                back_array.append(back_element)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_array}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()


    @classmethod
    def adminadvise(cls, **kwargs):
        showid=kwargs.get('ShowID')
        theaterid = kwargs.get('TheaterID')
        showname = kwargs.get('ShowName')
        description = kwargs.get('Description')
        showdate = kwargs.get('ShowDate')
        duration = kwargs.get('Duration')
        adminid = kwargs.get('AdminID')
        image = kwargs.get('Image')
        category = kwargs.get('Category')
        city = kwargs.get('City')

        try:

            existing_show = db.session.query(cls).filter_by(ShowID=showid).first()
            if existing_show is None:
                return {'code': RET.NODATA, 'message': error_map_EN[RET.NODATA], 'error': "修改演出不存在"}

            for attr_name in ['TheaterID','ShowName', 'Description', 'ShowDate', 'Duration', 'AdminID', 'Image', 'Category',
                              'City']:
                attr_value = kwargs.get(attr_name)
                if attr_value is not None:
                    setattr(existing_show, attr_name, attr_value)

            db.session.commit()

            # 获取新用户信息
            user_info = db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.ShowID == showid).first()

            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                    "ShowID": user_info['ShowID'],
                    "TheaterID": user_info['TheaterID'],
                    "ShowName": user_info['ShowName'],
                    "Description": user_info['Description'],
                    "ShowDate": user_info['ShowDate'],
                    "Duration": user_info['Duration'],
                    "AdminID": user_info['AdminID'],
                    "Image": user_info['Image'],
                    "Category": user_info['Category'],
                    "City": user_info['City'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()


    @classmethod
    def admindelete(cls, **kwargs):
        showid=kwargs.get('ShowID')

        try:

            existing_user = db.session.query(cls).filter_by(ShowID=showid).first()
            if existing_user is None:
                return {'code': RET.DATAEXIST, 'message': error_map_EN[RET.DATAEXIST], 'error': "想要删除的演出ID不存在"}

            user_info = db.session.query(
                cls.ShowID,
                cls.TheaterID,
                cls.ShowName,
                cls.Description,
                cls.ShowDate,
                cls.Duration,
                cls.AdminID,
                cls.Image,
                cls.Category,
                cls.City,
            ).filter(cls.ShowID==showid).first()


            db.session.delete(existing_user)
            db.session.commit()



            user_info = dict(user_info._asdict())

            db.session.close()

            back_dict = {
                    "ShowID": user_info['ShowID'],
                    "TheaterID": user_info['TheaterID'],
                    "ShowName": user_info['ShowName'],
                    "Description": user_info['Description'],
                    "ShowDate": user_info['ShowDate'],
                    "Duration": user_info['Duration'],
                    "AdminID": user_info['AdminID'],
                    "Image": user_info['Image'],
                    "Category": user_info['Category'],
                    "City": user_info['City'],
            }

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], "data": back_dict}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'error': str(e)}
        finally:
            db.session.close()
    pass
