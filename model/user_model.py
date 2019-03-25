# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:21
# @Author :garyhost
# @File :user_model.py
from config import db
import comm
from manage import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    object_id = db.Column(db.String, primary_key=True, unique=True, default=comm.create_primary_key())
    confirmed = db.Column(db.Boolean, default=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    # token = db.Column(db.String)

    # def generate_confirmation_token(self, expiration=3600):
    #     s = Serializer(app.config['SECRET_KEY'], expiration)
    #     return s.dumps(app.config['SECRET_KEY'])
    #
    # def confirm(self, token):
    #     s = Serializer(app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #     except:
    #         return False
    #     if data.get('confirm') != self.id:
    #         return False
    #     self.confirmed = True
    #     db.session.add(self)
    #     return True
