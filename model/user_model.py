# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:21
# @Author :garyhost
# @File :user_model.py
from app import db
from manage import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(db.Model):
    confirmed = db.Column(db.Boolean, default=False)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps(app.config['SECRET_KEY'])

    def confirm(self, token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
