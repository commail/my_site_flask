# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/22 17:18
# @Author :garyhost
# @File :blog.py
from flask import *
import model
from config import db

blue = Blueprint('v1/blog', 'blog')


@blue.route('/list/', methods=['GET'])
def blog_list():
    params = request.args
    skip = params.get('skip')
    count = params.get('count')
    blogs = model.Blog.query.skip(skip).limit(count).all()
    rv = []
    for blog in blogs:
        data = {
            'blogId': blog.object_id,
            'title': blog.title,
            'content': blog.content,
        }
        rv.append(data)
    return {
        'blogList': rv
    }


@blue.route('/create', methods=['POST'])
def blog_create():
    params = request.get_json()
    new_blog = model.Blog(title=params.title, content=params.content)
    db.session.add(new_blog)
    db.session.commit()
    return {}
