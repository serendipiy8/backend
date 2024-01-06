#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    gunicorn启动文件
"""

import os
import sys


def start():
    cmd = 'cd /my_project/my_api/;' \
          'gunicorn -c deploy/gunicorn.conf manage:app -D'
    os.system(cmd)


def stop():
    cmd = "ps -ef | grep 'gunicorn' | grep -v grep | awk '{print $2}' | xargs kill -9"
    os.system(cmd)


def restart():
    stop()
    start()


if sys.argv[1] == 'start':
    start()
elif sys.argv[1] == 'restart':
    restart()
elif sys.argv[1] == 'stop':
    stop()
else:
    print('params error!')
