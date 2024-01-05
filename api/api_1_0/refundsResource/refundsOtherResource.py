#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Resource
from service.refundsService import RefundsService
from flask_restful import Resource,reqparse
from flask import jsonify
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET


class RefundsOtherResource(Resource):
	@classmethod
	def refunds_post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID', type=str, location='form', required=True, help='用户ID数据类型不匹配')
		parser.add_argument('AdminID', type=str, location='form', required=True, help='管理员ID类型不匹配')
		parser.add_argument('RefundTime', type=str, location='form', required=True, help='投票时间类型不匹配')
		parser.add_argument('RefundReason', type=str, location='form', required=True, help='退票原因类型不匹配')
		parser.add_argument('TicketStatus', type=str, location='form', required=True, help='票状态类型不匹配')
		parser.add_argument('OrderID', type=str, location='form', required=True, help='订单ID类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = RefundsService.refunds_post(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])


	@classmethod
	def refunds_revise(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('RefundID', type=str, location='form', required=True, help='退票ID数据类型不匹配')
		parser.add_argument('TicketStatus', type=str, location='form', required=True, help='票状态类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = RefundsService.refunds_revise(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	@classmethod
	def refundsOrder(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('OrderID', type=str, location='form', required=True, help='剧院ID数据类型不匹配')

		try:
			# 获取请求中参数并转换为字典对象
			kwargs = parser.parse_args()
			# 去除字典中的None值
			kwargs = commons.put_remove_none(**kwargs)
		except Exception as e:
			loggings.exception(1, e)
			return jsonify(code=RET.PARAMERR, message="参数类型不正确或缺失", error="参数类型不正确或缺失")

		res = RefundsService.refundsOrder(**kwargs)

		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

		else:
			return jsonify(code=res['code'], message=res['message'], error=res['error'])

	pass
