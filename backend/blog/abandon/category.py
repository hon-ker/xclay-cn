#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from typing import List

from blog.db import engine, Base, SessionLocal
from blog import schemas
from blog.crud import category as category_crud
from utils import status

blog_category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@blog_category.get("/category/all", response_model=List[schemas.GetTag] | status.QueryError)
def get_category_by_name(db: Session = Depends(get_db)):
    db_category = category_crud.get_all_category(db)
    if db_category:
        return db_category

    return status.QueryError()


@blog_category.get("/category/{name}", response_model=schemas.GetTag | status.QueryError)
def get_category(name: str, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_name(db, name)
    if db_category:
        return db_category

    return status.QueryError()


@blog_category.get("/category/id/{category_id}", response_model=schemas.GetTag | status.QueryError)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_id(db, category_id)
    if db_category:
        return db_category
    return status.QueryError()

