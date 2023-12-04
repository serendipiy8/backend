#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

adminfunctions_blueprint = Blueprint('adminfunctions', __name__)

from . import urls
