#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

orders_blueprint = Blueprint('orders', __name__)

from . import urls
