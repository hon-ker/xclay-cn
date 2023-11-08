#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from sqlalchemy.orm import Session

from blog.models import Post, Tag, Category, User, Post
from blog.schemas import CreatePost, CreateTag, CreateCategory, CreateUser, UpdateUser, CreateDraft


# 数据库crud操作
def create_draft(db: Session, draft: CreateDraft):
    db_draft = Post(**draft.dict())
    db.add(db_draft)
    db.commit()
    db.refresh(db_draft)
    return True


def get_drafts(db: Session):
    return db.query(Post).filter().all()


def get_draft_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title == title).first()


def get_draft_by_id(db: Session, draft_id: int):
    return db.query(Post).filter(Post.id == draft_id).first()


def update_draft(db: Session, draft: CreateDraft):
    db_draft = db.query(Post).filter(Post.title == draft.title).first()
    if db_draft:
        db_draft.title = draft.title
        db_draft.content = draft.content
        db.commit()
        return True
    return False


def delete_draft_by_id(db: Session, id: int):
    db_draft = get_draft_by_id(db, id)
    if db_draft:
        db_draft.delete()
        db.commit()
        return True
    return False


def delete_draft_by_id(db: Session, title: str):
    db_draft = get_draft_by_title(db, title)
    if db_draft:
        db_draft.delete()
        db.commit()
        return True
    return False


#############################################################
# post操作
#############################################################

# 增
def create_post(db: Session, post: CreatePost):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return True


# 删
def delete_post(db: Session, post: CreatePost):
    db_post = db.query(Post).filter(Post.title == post.title).first()
    if db_post:
        db_post.delete()
        db.commit()
        return True

    return False


# 查
def get_post(db: Session):
    return db.query(Post).filter().all()


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title == title).first()


def get_post_by_user(db: Session, user: str):
    return db.query(Post).filter(Post.user.uname == user).all()


def get_post_by_tag(db: Session, tag: str):
    return db.query(Post).filter(Post.tag.any(Tag.name == tag)).all()


def get_post_by_category(db: Session, category: str):
    return db.query(Post).join(Post.category).filter(Category.name == category).all()


# 改
def update_post(db: Session, post: CreatePost):
    db_post = db.query(Post).filter(Post.title == post.title).first()
    if db_post:
        return True
    return False


#############################################################
# tag操作
#############################################################

def create_tag(db: Session, tag: CreateTag):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tag(db: Session):
    return db.query(Tag).filter().all()


def get_tag_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()


def get_all_tag(db: Session):
    return db.query(Tag).filter().all()


def delete_tag(db: Session, tag: CreateTag):
    db_post = db.query(Tag).filter(Tag.name == tag.name).first()
    if db_post:
        db_post.delete()
        db.commit()
        return True

    return False


#############################################################
# category操作
#############################################################

def create_category(db: Session, category: CreateCategory):
    db_tag = Category(**category.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_category(db: Session):
    return db.query(Category).filter().all()


def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()


def get_all_category(db: Session):
    return db.query(Category).filter().all()


