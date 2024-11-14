# -*- coding: utf-8 -*-
"""
system_model.py
"""

from datetime import datetime

from peewee import CharField, DateTimeField, BooleanField, AutoField

from admin_server.enums.config_key_enum import ConfigKeyEnum
from admin_server.model.base_model import BaseModel
from admin_server.utils import secret_util


class SystemModel(BaseModel):
    """系统配置"""
    id = AutoField(primary_key=True)

    # 键
    key = CharField(unique=True)

    # 值
    value = CharField()

    # 显示
    label = CharField()

    # 输入提示
    placeholder = CharField()

    # 对外显示值
    is_show_value = BooleanField(default=False, null=False)

    # 创建时间
    create_time = DateTimeField(default=datetime.now)

    # 更新时间
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'tb_system'


def init_table_data():
    """
    系统配置初始值
    :return:
    """
    data = [
        # 邮箱配置
        {
            'key': ConfigKeyEnum.MAIL_HOST,
            'value': 'smtp.163.com',
            'label': '发件邮箱服务器地址',
            'placeholder': '发件邮箱服务器地址',
            'is_show_value': True,
        },
        {
            'key': ConfigKeyEnum.MAIL_PORT,
            'value': '465',  # 25 或者 465(ssl)
            'label': '发件邮箱服务器端口',
            'placeholder': '发件邮箱服务器端口：25 或者 465(ssl)',
            'is_show_value': True,
        },
        {
            'key': ConfigKeyEnum.MAIL_ALIAS,
            'value': 'Domain Admin',
            'label': '发件人邮箱名称',
            'placeholder': '发件人邮箱名称',
            'is_show_value': True,
        },
        {
            'key': ConfigKeyEnum.MAIL_USERNAME,
            'value': '',
            'label': '发件人邮箱账号',
            'placeholder': '发件人邮箱账号',
            'is_show_value': True,
        },
        {
            'key': ConfigKeyEnum.MAIL_PASSWORD,
            'value': '',
            'label': '发件人邮箱密码',
            'placeholder': '发件人邮箱密码',
            'is_show_value': True,
        },

        {
            'key': ConfigKeyEnum.MAIL_SUBJECT,
            'value': '[ssl]证书过期时间汇总',
            'label': '邮件标题',
            'placeholder': '邮件标题',
            'is_show_value': True,
        },

        # 分 时 日 月 周，默认每天上午 10: 30 检测
        {
            'key': ConfigKeyEnum.SCHEDULER_CRON,
            'value': '30 10 * * *',
            'label': '定时检测时间（crontab 表达式）',
            'placeholder': '分 时 日 月 周',
            'is_show_value': True,
        },

        {
            'key': ConfigKeyEnum.SECRET_KEY,
            'value': secret_util.get_random_secret(),
            'is_show_value': False,
            'label': 'Token秘钥',
            'placeholder': '重新设置后所有用户的登录状态会退出'
        },
        {
            'key': ConfigKeyEnum.TOKEN_EXPIRE_DAYS,
            'value': 7,
            'is_show_value': True,
            'label': 'Token有效期（天）',
            'placeholder': 'Token有效期（天）'
        },
    ]

    SystemModel.insert_many(data).execute()
