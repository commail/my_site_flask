# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:15
# @Author :garyhost
# @File :config.py.py
import os
import flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
db = SQLAlchemy()
bootstrap = Bootstrap()
login = LoginManager()

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
basedir = os.path.abspath(os.path.dirname(__file__))


# 可上传文件判断
def allowed_file(filename):
    # 根据文件名后缀返回是否可以上传
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 数据库连接
def get_db_uri():
    # user = ''
    # password = ''
    # host = ''
    # port = ''
    # database = ''
    db_can = 'root&chum1304z&127.0.0.1&3306&my_web'
    db_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'
    user, password, host, port, database = db_can.split('&')
    return db_uri.format(user, password, host, port, database)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_db_uri()

    @staticmethod
    def init_app(app):
        bootstrap.init_app(app)
        db.init_app(app)
        migrate = Migrate(db=db)
        login.init_app(app)


class DevelopConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging

        # 错误处理
        # @app.errorhandler(Exception)
        # def handle_error(error):
        #     handler = logging.FileHandler('logs.log', encoding='utf-8')
        #     handler.setLevel(logging.DEBUG)
        #     logging_format = logging.Formatter(
        #         '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        #     handler.setFormatter(logging_format)
        #     print(error)
        #     app.logger.addHandler(handler)
        #     return '1111'

        # 请求前处理
        # @app.before_request
        # def before_request():
        #     path = flask.request.path
        #     method = flask.request.method

        # 请求后处理
        # @app.after_request
        # def after_request(response):
        #     return response


config = {
    'develop': DevelopConfig
}
