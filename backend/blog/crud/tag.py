#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from sqlalchemy.orm import Session

from blog.models import Tag
from blog.schemas import AdminCreateTag, AdminUpdateTag


#############################################################
# tag操作
#############################################################

def create_tag(db: Session, tag: AdminCreateTag):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag_by_id(db: Session, tag_id: int):
    db_tag = get_tag_by_id(db, tag_id)
    if db_tag:
        db.delete(db_tag)
        db.commit()
        return True
    return False


def get_tag_by_id(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


def get_tag_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()


def get_all_tag(db: Session):
    return db.query(Tag).filter().all()


def update_tag(db: Session, tag: AdminUpdateTag):
    db_tag = get_tag_by_id(db, tag.id)
    if db_tag:
        for key, value in tag.dict().items():
            if value is not None and value is not "string":
                setattr(db_tag, key, value)
        db.commit()
        return True
    return False
