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
            'createdAt': blog.created_at,
            'updatedAt': blog.updated_at,
        }
        rv.append(data)
    return {
        'blogList': rv
    }


@blue.route('/create/', methods=['POST'])
def blog_create():
    params = request.get_json()
    new_blog = model.Blog(title=params.title, content=params.content)
    db.session.add(new_blog)
    db.session.commit()
    return {}


@blue.route('/content/', methods=['GET'])
def blog_content():
    params = request.get_args
    bid = params.get('bid')
    blog = model.Blog.query.filter_by(object_id=bid).first()
    data = {
        'blogId': blog.object_id,
        'title': blog.title,
        'content': blog.content,
        'createdAt': blog.created_at,
        'updatedAt': blog.updated_at,
    }
    render_template()
