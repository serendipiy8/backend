#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.adminfunctionsService import AdminfunctionsService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET


class AdminfunctionsOtherResource(Resource):
	@classmethod
	def adminfunctions_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('Name', type=str, location='form', required=True, help='功能名字名字类型不匹配')
		parser.add_argument('Permissions', type=str, location='form', required=True, help='功能权限类型不匹配')
		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdminfunctionsService.adminfunctions_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])


	@classmethod
	def adminfunctions_revise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('FunctionID', type=str, location='form', required=True, help='功能ID数据类型不匹配')
		parser.add_argument('Name', type=str, location='form', required=True, help='功能名字名字类型不匹配')
		parser.add_argument('Permissions', type=str, location='form', required=True, help='功能权限类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdminfunctionsService.adminfunctions_revise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def adminfunctions_delete(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('FunctionID', type=str, location='form', required=True, help='功能ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdminfunctionsService.adminfunctions_delete(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def adminfunctions_query(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('FunctionID', type=str, location='form', required=True, help='功能ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = AdminfunctionsService.adminfunctions_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass

