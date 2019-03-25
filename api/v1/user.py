# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/25 15:52
# @Author :garyhost
# @File :user.py
from flask import *
from flask_login import current_user, login_user
import model
from config import db
blue = Blueprint('v1/user', 'user')


@blue.route('/login', methods=['POST'])
def login():
    params = request.get_json()
    un = params.get('username')
    pwd = params.get('password')
    user = model.User.query.filter_by(username=un).first()
    if pwd != user.get('password'):
        raise ValueError()
    return {
        'username': un,
    }
