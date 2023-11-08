#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from blog.db import engine, Base, SessionLocal
from blog.crud import post as draft_crud
from blog.crud import user as user_crud
from blog.crud import tag as tag_crud
from blog.crud import category as category_crud
from blog import schemas

from blog.schema import draft as draft_schema
from blog.models import Post
from utils import status

blog_draft = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@blog_draft.get("/draft/all", response_model=List[draft_schema.GetDraft] | status.QueryError)
def get_draft(db: Session = Depends(get_db)):
    db_drafts = draft_crud.get_all_draft(db)
    if db_drafts:
        result = []
        for db_draft in db_drafts:
            try:
                category = db_draft.category.name
            except AttributeError as e:
                category = "默认"

            # 创建 GetPostResponse 对象
            response = schemas.GetDraft(
                id=db_draft.id,
                title=db_draft.title,
                content=db_draft.content,
                des=db_draft.des,
                tag=[tag.name for tag in db_draft.tag],
                category=category,
                user=db_draft.user.name,
                ctime=str(db_draft.ctime),
                ltime=str(db_draft.ltime)
            )

            result.append(response)
        return result
    return status.QueryError()


@blog_draft.get("/draft/id/{draft_id}", response_model=draft_schema.GetDraft | status.QueryError)
def get_draft_by_id(draft_id: int, db: Session = Depends(get_db)):
    db_draft = draft_crud.get_draft_by_id(db, draft_id)
    if db_draft:
        try:
            category = db_draft.category.name
        except AttributeError as e:
            category = "默认"
        resp = schemas.GetDraft(
            id=db_draft.id,
            title=db_draft.title,
            content=db_draft.content,
            des=db_draft.des,
            tag=[tag.name for tag in db_draft.tag],
            category=category,
            user=db_draft.user.name,
            ctime=str(db_draft.ctime),
            ltime=str(db_draft.ltime)
        )
        return resp
    return status.QueryError()


@blog_draft.get("/draft/{title}", response_model=draft_schema.GetDraft | status.QueryError)
def get_draft_by_title(title: str, db: Session = Depends(get_db)):
    db_draft = draft_crud.get_draft_by_title(db, title)
    if db_draft:
        try:
            category = db_draft.category.name
        except AttributeError as e:
            category = "默认"

        resp = schemas.GetDraft(
            id=db_draft.id,
            title=db_draft.title,
            content=db_draft.content,
            des=db_draft.des,
            tag=[tag.name for tag in db_draft.tag],
            category=category,
            user=db_draft.user.name,
            ctime=str(db_draft.ctime),
            ltime=str(db_draft.ltime)
        )
        return resp
    return status.QueryError()


