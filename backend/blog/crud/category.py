#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from sqlalchemy.orm import Session

from blog.models import Category
from blog.schemas import AdminCreateCategory, AdminUpdateCategory


#############################################################
# category操作
#############################################################

def create_category(db: Session, category: AdminCreateCategory):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category_by_id(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()


def get_all_category(db: Session):
    return db.query(Category).filter().all()


def update_category(db: Session, category: AdminUpdateCategory):
    db_category = get_category_by_id(db, category.id)
    if db_category:
        for key, value in category.dict().items():
            if value is not None and value is not "string":
                setattr(db_category, key, value)
        db.commit()
        return True
    return False
