#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# orm模型
from sqlalchemy import Column, String, Integer, BigInteger, Date, DateTime, ForeignKey, func, TEXT, Boolean, Table
from sqlalchemy.orm import relationship

from .db import Base

# tag和post 多对多的中间表
tag_and_post = Table('tag_and_post', Base.metadata,
                     Column('post_id', Integer, ForeignKey('post.id')),
                     Column('tag_id', Integer, ForeignKey('tag.id'))
                     )


class Post(Base):
    __tablename__ = 'post'  # 数据表的表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(128), unique=True, index=True, nullable=False, comment='省/直辖市')
    content = Column(TEXT, nullable=False, comment='国家代码')
    des = Column(String(256), comment='省/直辖市', nullable=True)

    # 标签 多对多
    tag = relationship("Tag", secondary=tag_and_post, back_populates="post")
    # 分类 多对一
    category_id = Column(Integer, ForeignKey('category.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True,
                         default="默认")
    category = relationship("Category", back_populates="post")

    user_id = Column(Integer, ForeignKey('user.id', ondelete="SET NULL", onupdate="CASCADE"), nullable=True,
                     default="User")
    user = relationship("User", back_populates="post")

    ctime = Column(DateTime, server_default=func.now(), comment='创建时间')
    ltime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    # __mapper_args__ = {"order_by": ltime}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.title}_{self.user}'


# class Post(Base):
#     __tablename__ = 'post'  # 数据表的表名
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(128), unique=True, index=True, nullable=False, comment='省/直辖市')
#     content = Column(TEXT, nullable=False, comment='国家代码')
#
#     cover = Column(String(256), comment='省/直辖市')
#     des = Column(String(256), comment='省/直辖市')
#
#     # 标签 多对多
#     tag = relationship("Tag", secondary=tag_and_post, back_populates="post")
#     # 分类 多对一
#     category_id = Column(Integer, ForeignKey('category.id'))
#     category = relationship("Category", back_populates="post")
#
#     view = Column(BigInteger, nullable=False, comment='国家人口')
#     star = Column(BigInteger, nullable=False, comment='国家人口')
#
#     is_active = Column(Boolean, default=True)
#
#     # 用户 多对一
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship("User", back_populates="post")
#
#     ctime = Column(DateTime, server_default=func.now(), comment='创建时间')
#     ltime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')
#
#     # __mapper_args__ = {"order_by": ltime}  # 默认是正序，倒序加上.desc()方法
#
#     def __repr__(self):
#         return f'{self.title}_{self.user}'
#

class Tag(Base):
    __tablename__ = 'tag'  # 数据表的表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, index=True, nullable=False, comment='省/直辖市')
    des = Column(String(256), comment='省/直辖市')

    ctime = Column(DateTime, server_default=func.now(), comment='创建时间')

    post = relationship("Post", secondary=tag_and_post, back_populates="tag")
    ltime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    # __mapper_args__ = {"order_by": ctime}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.name}'


class Category(Base):
    __tablename__ = 'category'  # 数据表的表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, index=True, nullable=False, comment='省/直辖市')
    des = Column(String(256), comment='省/直辖市')

    ctime = Column(DateTime, server_default=func.now(), comment='创建时间')
    ltime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    # 文章 一对多
    post = relationship("Post", back_populates="category", lazy="dynamic")

    # __mapper_args__ = {"order_by": ctime}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.name}'


class User(Base):
    __tablename__ = 'user'  # 数据表的表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), unique=True, index=True, nullable=False, comment='省/直辖市')
    des = Column(String(256), nullable=True, comment='省/直辖市')
    passwd = Column(String(100), nullable=False, comment='国家代码')
    avatar = Column(String(100), nullable=True, comment='国家代码')
    mail = Column(String(256), nullable=True, comment='mail')
    token = Column(String(256), nullable=True, comment='token')

    # 文章 一对多
    post = relationship("Post", back_populates="user", lazy="dynamic")
    is_manager = Column(Boolean, nullable=True, default=False)
    # is_author = Column(Boolean, nullable=False, default=False)
    is_token_valid = Column(Boolean, nullable=True, default=True)

    ctime = Column(DateTime, server_default=func.now(), comment='创建时间')

    # __mapper_args__ = {"order_by": name}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.uname}_{self.is_manager}'


class Line(Base):
    __tablename__ = 'line'  # 数据表的表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(512), unique=True, index=True, nullable=False, comment='省/直辖市')
    author = Column(String(64), comment='省/直辖市', nullable=True)
    origin = Column(String(256), comment='省/直辖市', nullable=True)

    ctime = Column(DateTime, server_default=func.now(), comment='创建时间')
    ltime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    # __mapper_args__ = {"order_by": ctime}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.name}'
