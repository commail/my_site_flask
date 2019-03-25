# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:39
# @Author :garyhost
# @File :app.py
import flask
from config import config
import logging


def create_app(config_name):
    from api.v1 import user, blog
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route('/')
    def index():
        return flask.render_template('index.html')

    @app.route('/register')
    def register():
        return flask.render_template('register.html')
    app.register_blueprint(user.blue, url_perfix='/v1/user')
    # app.register_blueprint(blog.blue, url_perfix='/v1/blog')

    return app
