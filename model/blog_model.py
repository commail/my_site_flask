# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/22 17:18
# @Author :garyhost
# @File :blog_model.py
from app import db
import comm
import datetime


class Blog(db.Model):
    __tablename__ = 'blog'
    object_id = db.Column(db.String, primary_key=True, unique=True, default=comm.create_primary_key())
    user = db.relationship('User')
    content = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.datetime.now())
    updated_at = db.Column(db.Datetime, default=datetime.datetime.now())
