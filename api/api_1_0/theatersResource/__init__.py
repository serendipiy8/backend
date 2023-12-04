#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

theaters_blueprint = Blueprint('theaters', __name__)

from . import urls
