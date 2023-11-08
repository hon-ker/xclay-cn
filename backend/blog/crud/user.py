#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from sqlalchemy.orm import Session

from blog.models import User
from blog.schemas import Login, Register, UpdateUser

from blog.auth import pwd_context


#############################################################
# user操作
#############################################################

def create_user(db: Session, user: Register):
    user.passwd = pwd_context.hash(user.passwd)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def is_user(db: Session, user: Login):
    user.passwd = pwd_context.hash(user.passwd)
    return db.query(User).filter(User.name == user.name, User.passwd == user.passwd).first()


def get_all_user(db: Session):
    return db.query(User).filter().all()


def update_user(db: Session, user: UpdateUser):
    if user.passwd:
        user.passwd = pwd_context.hash(user.passwd)
    db_user = get_user_by_id(db, user.id)

    if db_user:
        for key, value in user.dict().items():

            if value is not None:
                setattr(db_user, key, value)
        db.commit()
        return True
    return False
