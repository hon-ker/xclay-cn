#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import List
from blog.db import engine, Base, SessionLocal
from blog import schemas
from blog.crud import tag as tag_crud
from utils import status

blog_tag = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@blog_tag.get("/tag/all", response_model=List[schemas.GetTag] | status.QueryError)
def get_tag(db: Session = Depends(get_db)):
    db_tag = tag_crud.get_all_tag(db)
    if db_tag:
        return db_tag
    return status.QueryError()


@blog_tag.get("/tag/{name}", response_model=schemas.GetTag | status.QueryError)
def get_tag_by_name(name: str, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_name(db, name)
    if db_tag:
        return db_tag
    return status.QueryError()


@blog_tag.get("/tag/id/{tag_id}", response_model=schemas.GetTag | status.QueryError)
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_id(db, tag_id)
    if db_tag:
        return db_tag
    return status.QueryError()



