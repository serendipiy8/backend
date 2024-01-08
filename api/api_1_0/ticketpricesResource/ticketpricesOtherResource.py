#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.ticketpricesService import TicketpricesService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET

class TicketpricesOtherResource(Resource):

	@classmethod
	def ticketpricesQuery(cls):
		parser=reqparse.RequestParser()
		parser.add_argument('ShowID', type=str, location='form', required=True, help='票ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TicketpricesService.ticketpricesQuery(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])
	pass

	@classmethod
	def ticketprices_query(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TicketID', type=str, location='args', required=True, help='票ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TicketpricesService.ticketprices_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass

	@classmethod
	def ticketprices_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('ShowID',type=str,location='form',required=True,help='演出ID数据类型不匹配')
		parser.add_argument('Price',type=str,location='form',required=True,help='类型不匹配')
		parser.add_argument('Category',type=str,location='form',required=True,help='密码类型不匹配')
		parser.add_argument('TotalQuantity',type=str,location='form',required=True,help='密码类型不匹配')
		parser.add_argument('RemainingQuantity',type=str,location='form',required=True,help='密码类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TicketpricesService.ticketprices_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass

	@classmethod
	def ticketprices_put(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TicketID', type=str, location='form', required=True, help='票id数据类型不匹配')
		parser.add_argument('ShowID', type=str, location='form', required=True, help='演出ID数据类型不匹配')
		parser.add_argument('Price', type=str, location='form', required=True, help='价格类型不匹配')
		parser.add_argument('Category', type=str, location='form', required=True, help='类别类型不匹配')
		parser.add_argument('TotalQuantity', type=str, location='form', required=True, help='总数量类型不匹配')
		parser.add_argument('RemainingQuantity', type=str, location='form', required=True, help='剩余数量类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TicketpricesService.ticketprices_put(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass

	@classmethod
	def ticketprices_del(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('TicketID', type=str, location='form', required=True, help='票id数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = TicketpricesService.ticketprices_del(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])
		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass