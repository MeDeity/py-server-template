# -*- coding: utf-8 -*-
"""
@File    : ip_api.py
@Date    : 2022-10-14
@Author  : Peng Shiyu
"""
from flask import request

from admin_server.utils import ip_util


def get_ip_info():
    """
    获取ip地址的信息
    :return:
    """
    ip = request.json['ip']
    return ip_util.get_ip_info(ip)
