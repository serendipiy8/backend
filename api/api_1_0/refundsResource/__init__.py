#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

refunds_blueprint = Blueprint('refunds', __name__)

from . import urls
