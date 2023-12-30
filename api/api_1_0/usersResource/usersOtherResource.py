#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from flask_restful import Resource,reqparse
from flask import jsonify
from service.usersService import UsersService
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET

class UsersOtherResource(Resource):

	@classmethod
	def login(cls):
		parser=reqparse.RequestParser()
		parser.add_argument('account',type=str,location='form',required=True,help='账户数据类型不匹配')
		parser.add_argument('password',type=str,location='form',required=True,help='密码类型不匹配')


		try:
			# 获取请求中参数并转换为字典对象
			kwargs=parser.parse_args()
			# 去除字典中的None值
			kwargs=commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res=UsersService.login(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def register(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('account', type=str, location='form', required=True, help='账户数据类型不匹配')
		parser.add_argument('password', type=str, location='form', required=True, help='密码类型不匹配')
		parser.add_argument('password_again',type=str,location='form',required=True,help='密码类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = UsersService.register(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def information_post(cls):
		parser=reqparse.RequestParser()
		parser.add_argument('UserID', type=str, location='form', required=True, help='用户id数据类型不匹配')
		parser.add_argument('RealName', type=str, location='form', required=True, help='用户名数据类型不匹配')
		parser.add_argument('Gender', type=str, location='form', required=True, help='性别数据类型不匹配')
		parser.add_argument('IDcard', type=str, location='form', required=True, help='身份证号数据类型不匹配')
		parser.add_argument('Address', type=str, location='form', required=True, help='地址数据类型不匹配')
		parser.add_argument('Account', type=str, location='form', required=True, help='电话数据类型不匹配')
		parser.add_argument('Email', type=str, location='form', required=True, help='邮件数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = UsersService.information_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def information_query(cls):
		parser=reqparse.RequestParser()
		parser.add_argument('UserID', type=str, location='form', required=True, help='用户id数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = UsersService.information_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])