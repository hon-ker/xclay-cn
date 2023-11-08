#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from typing import List, Optional, Union

from blog.db import engine, Base, SessionLocal
from blog import schemas, auth
from blog.crud import user as user_crud
from utils import status

blog_user = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@blog_user.get("/user/all", response_model=List[schemas.GetUser] | status.Base)
def get_user_by_name(db: Session = Depends(get_db)):
    db_user = user_crud.get_all_user(db)
    if db_user:
        return db_user
    return status.QueryError


@blog_user.get("/user/{name}", response_model=schemas.GetUser | status.Base)
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, name)
    if db_user:
        return db_user
    return status.QueryError


@blog_user.get("/user/id/{user_id}", response_model=schemas.GetUser | status.Base)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user:
        return db_user
    return status.QueryError


@blog_user.put(f"/user")
def update_draft_by_id(user: schemas.UpdateUser, db: Session = Depends(get_db)):
    db_user = user_crud.update_user(db, user)
    if db_user:
        return status.UpdateSuccess()
    return status.UpdateError()


# 用户认证
@blog_user.post(f"/login")
def login(user: schemas.Login, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, user.name)

    if db_user and auth.pwd_context.verify(user.passwd, db_user.passwd):
        # 登录成功，生成token并添加到cookie中
        access_token = auth.create_access_token(data={"name": db_user.name, "is_manager": db_user.is_manager})
        response = JSONResponse(content=status.ActionSuccess(msg="登录成功!").model_dump())
        # response = JSONResponse(content=status.ActionSuccess(msg="登录成功!").dict())
        response.set_cookie(key="token", value=access_token, httponly=True)  # 将token设置为httponly的cookie
        return response

    return status.ActionError(msg="登录失败!")


@blog_user.post(f"/register")
def register(user: schemas.Register, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, user.name)
    if db_user:
        return status.AlreadyExistError(msg="用户名已占用!")
    db_user = user_crud.create_user(db, user)
    if db_user:
        access_token = auth.create_access_token(data={"name": db_user.name, "is_manager": db_user.is_manager})
        response = JSONResponse(content=status.ActionSuccess(msg="注册成功!").dict())
        response.set_cookie(key="token", value=access_token, httponly=True)  # 将token设置为httponly的cookie
        return response

    return status.ActionError(msg="注册失败!")
