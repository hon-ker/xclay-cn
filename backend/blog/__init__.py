#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'


# from blog.abandon.apis import blog
# from .api.draft import blog_draft
# from .api.user import blog_user
# from .api.category import blog_category
# from .api.tag import blog_tag
from .api.admin import blog_admin
from .api.ordinary import blog_ordinary

from blog.db import engine, Base, SessionLocal
from blog.models import Post, Category, Tag, User

# 创建数据库，初始化数据
Base.metadata.create_all(bind=engine)
