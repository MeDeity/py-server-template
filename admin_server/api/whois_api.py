# -*- coding: utf-8 -*-
"""
@File    : whois_api.py
@Date    : 2023-06-01
"""
from flask import request

from admin_server.utils import whois_util


def get_whois_raw():
    """
    获取域名信息原始
    :return:
    """
    domain = request.json['domain']
    resolve_domain = whois_util.resolve_domain(domain)
    raw_data = whois_util.get_domain_raw_whois(resolve_domain)

    return {
        "domain": domain,
        "resolve_domain": resolve_domain,
        "raw_data": raw_data
    }
