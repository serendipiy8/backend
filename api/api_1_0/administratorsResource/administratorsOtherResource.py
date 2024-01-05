#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.administratorsService import AdministratorsService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET

class AdministratorsOtherResource(Resource):

	@classmethod
	def administrators_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('AdminType', type=str, location='form', required=True, help='管理员类型数据类型不匹配')
		parser.add_argument('Account', type=str, location='form', required=True, help='输入账号类型不匹配')
		parser.add_argument('Password', type=str, location='form', required=True, help='输入密码类型不匹配')
		parser.add_argument('Permissions', type=str, location='form', required=True, help='管理员权限数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdministratorsService.administrators_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def administrators_query(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdministratorsService.administrators_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def administrators_revise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')
		parser.add_argument('AdminType', type=str, location='form', required=True, help='管理员类型数据类型不匹配')
		parser.add_argument('Account', type=str, location='form', required=True, help='输入账号类型不匹配')
		parser.add_argument('Password', type=str, location='form', required=True, help='输入密码类型不匹配')
		parser.add_argument('Permissions', type=str, location='form', required=True, help='管理员权限数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdministratorsService.administrators_revise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def administrators_delete(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdministratorsService.administrators_delete(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass
