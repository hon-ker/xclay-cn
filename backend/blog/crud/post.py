#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from sqlalchemy.orm import Session

from blog.models import Post

from blog.schemas import GetPost, AdminCreatePost


# 数据库crud操作
def create_post(db: Session, post: AdminCreatePost):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return True


def get_all_post(db: Session):
    return db.query(Post).filter().all()


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title == title).first()


def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def update_post_by_id(db: Session, post: GetPost):
    db_post = get_post_by_id(db, post.id)
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db_post.category = post.category
        db_post.tag = post.tag
        db.commit()
        return True
    return False


def update_post_by_title(db: Session, post: GetPost):
    db_post = get_post_by_title(db, post.title)
    if db_post:
        for key, value in post.dict().items():
            if value is not None and value is not "string":
                setattr(db_post, key, value)
        db.commit()
        return True
    return False


def delete_post_by_id(db: Session, post_id: int):
    db_post = get_post_by_id(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False


def delete_post_by_title(db: Session, title: str):
    db_post = get_post_by_title(db, title)
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False
