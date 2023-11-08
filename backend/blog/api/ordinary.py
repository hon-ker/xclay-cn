#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'
from typing import List
from fastapi import APIRouter, Depends, Body, Cookie, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from blog.db import engine, Base, SessionLocal
from blog.crud import post as post_crud
from blog.crud import user as user_crud
from blog.crud import tag as tag_crud
from blog.crud import category as category_crud
from blog import schemas, auth

from utils import status

blog_ordinary = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#################################################
# 文章
#################################################


@blog_ordinary.get("/post/all", response_model=List[schemas.GetPost] | status.QueryError)
def get_post(db: Session = Depends(get_db)):
    db_posts = post_crud.get_all_post(db)
    if db_posts:
        result = []
        for db_post in db_posts:
            try:
                category = db_post.category.name
            except AttributeError as e:
                category = "默认"

            # 创建 GetPostResponse 对象
            response = schemas.GetPost(
                title=db_post.title,
                content=db_post.content,
                des=db_post.des,
                tag=[tag.name for tag in db_post.tag],
                category=category,
                user=db_post.user.name,
                ctime=str(db_post.ctime),
                ltime=str(db_post.ltime)
            )

            result.append(response)
        return result
    return status.QueryError()


@blog_ordinary.get("/post/{title}", response_model=schemas.GetPost | status.QueryError)
def get_post_by_title(title: str, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_title(db, title)
    if db_post:
        try:
            category = db_post.category.name
        except AttributeError as e:
            category = "默认"

        resp = schemas.GetPost(
            title=db_post.title,
            content=db_post.content,
            des=db_post.des,
            tag=[tag.name for tag in db_post.tag],
            category=category,
            user=db_post.user.name,
            ctime=str(db_post.ctime),
            ltime=str(db_post.ltime)
        )
        return resp
    return status.QueryError()


#################################################
# 用户
#################################################
@blog_ordinary.get("/user/all", response_model=List[schemas.GetUser] | status.Base)
def get_all_user(db: Session = Depends(get_db)):
    db_user = user_crud.get_all_user(db)
    if db_user:
        return db_user
    return []


@blog_ordinary.get("/user/{name}", response_model=schemas.GetUser | status.Base)
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, name)
    if db_user:
        return db_user
    return status.QueryError


@blog_ordinary.put(f"/user/id")
def update_user_by_id(user: schemas.UpdateUser, db: Session = Depends(get_db)):
    # db_user = user_crud.update_user(db, user)
    # if db_user:
    #     return status.UpdateSuccess()
    return status.ActionError(msg="#TODO: 非管理员更新自己信息")


# 是否已登录
@blog_ordinary.get(f"/is_login")
def is_login(token: str = Cookie(default="token"), db: Session = Depends(get_db)):
    token = auth.get_decoded_token(token)
    if token:
        name = token.get("name")
        db_user = user_crud.get_user_by_name(db, name)
        print(db_user.name)

        if db_user:
            return {"is_login": True}
    return {"is_login": False}


# 用户认证
@blog_ordinary.post(f"/login")
def login(user: schemas.Login, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, user.name)

    if db_user and auth.pwd_context.verify(user.passwd, db_user.passwd):
        # 登录成功，生成token并添加到cookie中
        access_token = auth.create_access_token(data={"name": db_user.name, "is_manager": db_user.is_manager})
        response = JSONResponse(content=status.ActionSuccess(msg="登录成功!").model_dump())
        # response = JSONResponse(content=status.ActionSuccess(msg="登录成功!").dict())
        response.set_cookie(key="token", value=access_token, httponly=True)  # 将token设置为httponly的cookie
        return response

    raise HTTPException(status_code=401, detail="登录失败!")


@blog_ordinary.get("/logout")
def logout():
    response = JSONResponse(content=status.ActionSuccess(msg="退出登录成功!").model_dump())
    response.delete_cookie(key="token")  # 清除名为 "token" 的cookie
    return response


@blog_ordinary.post(f"/register")
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


#################################################
# 分类
#################################################
@blog_ordinary.get("/category/all", response_model=List[schemas.GetTag] | status.QueryError)
def get_category_by_name(db: Session = Depends(get_db)):
    db_category = category_crud.get_all_category(db)
    if db_category:
        return db_category

    return status.QueryError()


@blog_ordinary.get("/category/{name}", response_model=schemas.GetTag | status.QueryError)
def get_category(name: str, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_name(db, name)
    if db_category:
        return db_category

    return status.QueryError()


#################################################
# 标签
#################################################


@blog_ordinary.get("/tag/all", response_model=List[schemas.GetTag] | status.QueryError)
def get_tag(db: Session = Depends(get_db)):
    db_tag = tag_crud.get_all_tag(db)
    if db_tag:
        return db_tag
    return status.QueryError()


@blog_ordinary.get("/tag/{name}", response_model=schemas.GetTag | status.QueryError)
def get_tag_by_name(name: str, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_name(db, name)
    if db_tag:
        return db_tag
    return status.QueryError()
