#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

shows_blueprint = Blueprint('shows', __name__)

from . import urls
