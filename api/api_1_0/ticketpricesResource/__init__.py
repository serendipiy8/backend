#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

ticketprices_blueprint = Blueprint('ticketprices', __name__)

from . import urls
