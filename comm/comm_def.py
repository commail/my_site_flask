# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/22 17:21
# @Author :garyhost
# @File :comm_def.py
import uuid


# 生成主键
def create_primary_key():
    return uuid.uuid1()
