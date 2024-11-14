# -*- coding: utf-8 -*-
"""
database.py
"""

# 创建表
from admin_server.log import logger
from admin_server.model.base_model import db
from admin_server.model import domain_model
from admin_server.model import address_model
from admin_server.model import domain_info_model
from admin_server.model import group_model
from admin_server.model import system_model
from admin_server.model import user_model
from admin_server.model import log_scheduler_model
from admin_server.model import notify_model
from admin_server.model import version_model
from admin_server.model import cache_domain_info_model

# 需要查询初始数据操作的表放前面
tables = [
    (system_model.SystemModel, system_model.init_table_data),
    (version_model.VersionModel, None),
    (user_model.UserModel, user_model.init_table_data),
    (log_scheduler_model.LogSchedulerModel, None),
    (group_model.GroupModel, None),
    (domain_model.DomainModel, None),
    (notify_model.NotifyModel, None),
    (cache_domain_info_model.CacheDomainInfoModel, None),
    (address_model.AddressModel, None),
    (domain_info_model.DomainInfoModel, None),
]


def init_database():
    db.connect()

    for model, init_func in tables:
        if not model.table_exists():
            logger.debug('create table: %s', model._meta.table_name)
            model.create_table()

            if init_func:
                init_func()

    db.close()
