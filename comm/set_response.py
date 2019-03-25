# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/25 19:07
# @Author :garyhost
# @File :set_response.py
from flask import Response, jsonify


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(MyResponse, cls).force_type(response, environ)
