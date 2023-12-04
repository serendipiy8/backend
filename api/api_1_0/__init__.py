#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .apiVersionResource import apiversion_blueprint
from .adminfunctionsResource import adminfunctions_blueprint
from .showsResource import shows_blueprint
from .refundsResource import refunds_blueprint
from .ordersResource import orders_blueprint
from .administratorsResource import administrators_blueprint
from .ticketpricesResource import ticketprices_blueprint
from .theatersResource import theaters_blueprint
from .usersResource import users_blueprint


def init_router(app):
    from api_1_0.apiVersionResource import apiversion_blueprint
    app.register_blueprint(apiversion_blueprint, url_prefix="/")

    # adminfunctions blueprint register
    from api_1_0.adminfunctionsResource import adminfunctions_blueprint
    app.register_blueprint(adminfunctions_blueprint, url_prefix="/")
    
    # shows blueprint register
    from api_1_0.showsResource import shows_blueprint
    app.register_blueprint(shows_blueprint, url_prefix="/")
    
    # refunds blueprint register
    from api_1_0.refundsResource import refunds_blueprint
    app.register_blueprint(refunds_blueprint, url_prefix="/")
    
    # orders blueprint register
    from api_1_0.ordersResource import orders_blueprint
    app.register_blueprint(orders_blueprint, url_prefix="/")
    
    # administrators blueprint register
    from api_1_0.administratorsResource import administrators_blueprint
    app.register_blueprint(administrators_blueprint, url_prefix="/")
    
    # ticketprices blueprint register
    from api_1_0.ticketpricesResource import ticketprices_blueprint
    app.register_blueprint(ticketprices_blueprint, url_prefix="/")
    
    # theaters blueprint register
    from api_1_0.theatersResource import theaters_blueprint
    app.register_blueprint(theaters_blueprint, url_prefix="/")

    # users blueprint register
    from api_1_0.usersResource import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix="/")
    
