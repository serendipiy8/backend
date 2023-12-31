#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
   应用初始化文件模板
"""

from flask import Flask
from flask_session import Session
from .setting import Settings
from models import db

# 工厂模式创建app应用对象
def create_app(run_mode):
    """
    创建flask的应用对象
    :param run_mode: string 配置模式的名字  （"develop", "product", "test"）
    :return:
    """
    
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    app.config.from_object(Settings.get_setting(run_mode))

    # 使用app初始化db
    db.init_app(app)

    # 利用Flask_session将数据保存的session中
    Session(app)

    # 调用resource层中定义的方法，初始化所有路由(注册)蓝图
    from api_1_0 import init_router
    init_router(app)
    
    return app
