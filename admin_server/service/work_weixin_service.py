# -*- coding: utf-8 -*-
"""
@File    : work_weixin_service.py
@Date    : 2023-03-08
"""
import json

from admin_server.enums.notify_type_enum import NotifyTypeEnum
from admin_server.log import logger
from admin_server.service import notify_service
from admin_server.utils import work_weixin_api


def send_work_weixin_message(user_id):
    """
    发送企业微信消息
    :param user_id:
    :return:
    """
    notify_row_value = notify_service.get_notify_row_value(user_id, NotifyTypeEnum.WORK_WEIXIN)
    if not notify_row_value:
        return None

    corpid = notify_row_value.get('corpid')
    corpsecret = notify_row_value.get('corpsecret')
    body = notify_row_value.get('body')

    token = work_weixin_api.get_access_token(corpid, corpsecret)
    logger.debug('token %s', token)
    res = work_weixin_api.send_message(token['access_token'], json.loads(body))
    return res

