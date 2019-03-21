# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:15
# @Author :garyhost
# @File :config.py.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


# 可上传文件判断
def allowed_file(filename):
    # 根据文件名后缀返回是否可以上传
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_db_uri():
    # user = ''
    # password = ''
    # host = ''
    # port = ''
    # database = ''
    db_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'
    user, password, host, port, database = os.environ['DATABASE'].split('&')
    print(db_uri.format(user, password, host, port, database))
    return db_uri.format(user, password, host, port, database)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_uri()


config = {
    'develop': DevelopConfig
}
