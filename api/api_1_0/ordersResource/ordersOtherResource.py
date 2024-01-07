#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service.ordersService import OrdersService
from flask_restful import Resource
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET

class OrdersOtherResource(Resource):
	@classmethod
	def orders_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID', type=str, location='form', required=True, help='用户ID数据类型不匹配')
		parser.add_argument('TicketID', type=str, location='form', required=True, help='票ID类型不匹配')
		parser.add_argument('PurchaseTime', type=str, location='form', required=True, help='支付时间类型不匹配')
		parser.add_argument('OrderStatus', type=str, location='form', required=True, help='订单状态数据类型不匹配')
		parser.add_argument('Quantity', type=str, location='form', required=True, help='票数量数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = OrdersService.orders_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def orders_query(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('OrderID', type=str, location='form', required=True, help='订单ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = OrdersService.orders_query(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def queryUser(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID', type=str, location='form', required=True, help='订单ID数据类型不匹配')

		try:
				# 获取请求中参数并转换为字典对象
				kwargs = parser.parse_args()
				# 去除字典中的None值
				kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = OrdersService.queryUser(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

		pass

	@classmethod
	def orders_revise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('OrderID', type=str, location='form', required=True, help='订单ID数据类型不匹配')
		parser.add_argument('OrderStatus', type=str, location='form', required=True, help='订单状态类型数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = OrdersService.orders_revise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	# @classmethod
	# def administrators_delete(cls):
	# 	parser = reqparse.RequestParser()
	# 	parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID数据类型不匹配')
	#
	# 	try:
	# 		# 获取请求中参数并转换为字典对象
	# 		kwargs = parser.parse_args()
	# 		# 去除字典中的None值
	# 		kwargs = commons.put_remove_none(**kwargs)
	# 	except Exception as e:
	# 		loggings.exception(1, e)
	# 		return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")
	#
	# 	res = AdministratorsService.administrators_delete(**kwargs)
	#
	# 	if res['code'] == RET.OK:
	# 		return jsonify(code=res['code'], message=res['message'], data=res['data'])
	#
	# 	else:
	# 		return jsonify(code=res['code'], message=res['message'], error=res['error'])
	#
	# pass
