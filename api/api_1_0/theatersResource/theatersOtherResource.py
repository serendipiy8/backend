#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.theatersService import TheatersService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET


class TheatersOtherResource(Resource):

	@classmethod
	def theaters_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterName', type=str, location='form', required=True, help='剧院名字数据类型不匹配')
		parser.add_argument('Address', type=str, location='form', required=True, help='剧院地址类型不匹配')
		parser.add_argument('Capacity', type=str, location='form', required=True, help='剧院容量类型不匹配')
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TheatersService.theaters_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def theaters_query(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterID', type=str, location='args', required=True, help='剧院ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TheatersService.theaters_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])



	@classmethod
	def theaters_revise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterID', type=str, location='form', required=True, help='剧院ID数据类型不匹配')
		parser.add_argument('TheaterName', type=str, location='form', required=True, help='剧院名字类型不匹配')
		parser.add_argument('Address', type=str, location='form', required=True, help='地址类型不匹配')
		parser.add_argument('Capacity', type=str, location='form', required=True, help='容量类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TheatersService.theaters_revise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])


	@classmethod
	def theaters_delete(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterID', type=str, location='args', required=True, help='剧院ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TheatersService.theaters_delete(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])
	pass
