#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.showsService import ShowsService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET

class ShowsOtherResource(Resource):

	@classmethod
	def adminpost(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterID', type=str, location='form', required=True, help='剧院ID数字类型不匹配')
		parser.add_argument('ShowName', type=str, location='form', required=True, help='演出名字数字类型不匹配')
		parser.add_argument('Description', type=str, location='form', required=True, help='演出描述类型不匹配')
		parser.add_argument('ShowDate', type=str, location='form', required=True, help='演出日期类型不匹配')
		parser.add_argument('Duration', type=str, location='form', required=True, help='演出时长类型不匹配')
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')
		parser.add_argument('Image', type=str, location='form', required=True, help='图片URL数据类型不匹配')
		parser.add_argument('Category', type=str, location='form', required=True, help='演出类别数据类型不匹配')
		parser.add_argument('City', type=str, location='form', required=True, help='演出城市数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.adminpost(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def queryShowID(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('ShowID', type=str, location='form', required=True, help='演出ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.queryShowID(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def queryShowName(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('ShowName', type=str, location='form', required=True, help='演出数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.queryShowName(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def queryTheaterID(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TheaterID', type=str, location='form', required=True, help='剧院ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.queryTheaterID(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def adminadvise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('ShowID', type=str, location='form', required=True, help='剧院ID数字类型不匹配')
		parser.add_argument('TheaterID', type=str, location='form', required=True, help='剧院ID数字类型不匹配')
		parser.add_argument('ShowName', type=str, location='form', required=True, help='演出名字数字类型不匹配')
		parser.add_argument('Description', type=str, location='form', required=True, help='演出描述类型不匹配')
		parser.add_argument('ShowDate', type=str, location='form', required=True, help='演出日期类型不匹配')
		parser.add_argument('Duration', type=str, location='form', required=True, help='演出时长类型不匹配')
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')
		parser.add_argument('Image', type=str, location='form', required=True, help='图片URL数据类型不匹配')
		parser.add_argument('Category', type=str, location='form', required=True, help='演出类别数据类型不匹配')
		parser.add_argument('City', type=str, location='form', required=True, help='演出城市数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.adminadvise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def admindelete(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('ShowID', type=str, location='form', required=True, help='演出ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = ShowsService.admindelete(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])
