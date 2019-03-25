# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/22 17:18
# @Author :garyhost
# @File :blog_model.py
from config import db
import comm
import datetime


class Blog(db.Model):
    __tablename__ = 'blog'
    object_id = db.Column(db.String(64), primary_key=True, unique=True, default=comm.create_primary_key())
    user = db.Column(db.String(64), db.ForeignKey('user.object_id'))
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    is_available = db.Column(db.Boolean, default=True)
