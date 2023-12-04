#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

administrators_blueprint = Blueprint('administrators', __name__)

from . import urls
