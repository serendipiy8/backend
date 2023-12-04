#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

users_blueprint = Blueprint('users', __name__)

from . import urls
