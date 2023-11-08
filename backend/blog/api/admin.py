#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from typing import List
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from blog.db import engine, Base, SessionLocal
from blog.crud import post as post_crud
from blog.crud import user as user_crud
from blog.crud import tag as tag_crud
from blog.crud import category as category_crud
from blog import schemas

from blog.models import Post
from utils import status

blog_admin = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#################################################
# 新增
#################################################

@blog_admin.post("/post")
def create_post(post: schemas.AdminCreatePost, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_title(db, post.title)
    if db_post:
        return status.AlreadyExistError(msg="草稿已存在")

    db_post = Post(title=post.title, content=post.content)
    db_user = user_crud.get_user_by_name(db, post.user)

    # 用户不存在
    if not db_user:
        return status.NotFoundError(msg="用户不存在!")
    # 用户不是管理员
    if not db_user.is_manager:
        return status.PermissionError()

    # 创建tag
    db_tags = []
    for tag_name in post.tag:
        schema_tag = schemas.AdminCreateTag(name=tag_name)
        db_tag = tag_crud.get_tag_by_name(db, tag_name)
        if not db_tag:
            db_tag = tag_crud.create_tag(db, schema_tag)
        db_tags.append(db_tag)

    # 查询category
    db_category = category_crud.get_category_by_name(db, post.category)
    if not db_category:
        schema_category = schemas.AdminCreateCategory(name=post.category)
        db_category = category_crud.create_category(db, schema_category)
        if not db_category:
            return status.CreateError(msg="新分类创建失败!")

    # 摘要
    db_post.des = post.des
    # 分类
    db_post.category = db_category
    db_post.category_id = db_category.id
    # 标签
    db_post.tag.clear()
    db_post.tag.extend(db_tags)
    # 作者
    db_post.user = db_user
    db_post.user_id = db_user.id
    # 提交数据
    db.add_all([*db_tags, db_post])
    db.commit()

    return status.CreateSuccess()


@blog_admin.post("/user")
def create_user(user: schemas.AdminCreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, user.name)
    if db_user:
        return status.AlreadyExistError()

    is_success = user_crud.create_user(db, user)
    if is_success:
        return status.CreateSuccess()

    return status.CreateError()


@blog_admin.post("/category")
def create_category(category: schemas.AdminCreateCategory, db: Session = Depends(get_db)):
    db_tag = category_crud.get_category_by_name(db, category.name)
    if db_tag:
        return status.AlreadyExistError()

    is_success = category_crud.create_category(db, category)
    if is_success:
        return status.CreateSuccess()

    return status.CreateError()


@blog_admin.post("/tag")
def create_tag(tag: schemas.AdminCreateTag, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_name(db, tag.name)
    if db_tag:
        return status.AlreadyExistError()

    is_success = tag_crud.create_tag(db, tag)
    if is_success:
        return status.CreateSuccess()

    return status.CreateError()


#################################################
# 删除
#################################################
@blog_admin.delete("/post/{title}")
def delete_post_by_title(title: str, db: Session = Depends(get_db)):
    is_success = post_crud.delete_post_by_title(db, title)
    if is_success:
        return status.DeleteSuccess()
    return status.DeleteError()


@blog_admin.delete("/post/id/{post_id}")
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    is_success = post_crud.delete_post_by_id(db, post_id)
    if is_success:
        return status.DeleteSuccess()
    return status.DeleteError()


# 删除user
@blog_admin.delete("/user/id/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if not db_user:
        return status.NotFoundError()

    is_success = user_crud.delete_user_by_id(db, user_id)
    if is_success:
        return status.DeleteSuccess()

    return status.DeleteError()


# 删除category
@blog_admin.delete("/category/id/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_id(db, category_id)
    if not db_category:
        return status.NotFoundError()
    if db_category.name == "默认" or db_category.name == "default":
        return status.PermissionError(msg="不允许删除!")
    is_success = category_crud.delete_category_by_id(db, category_id)

    if is_success:
        return status.DeleteSuccess()

    return status.DeleteError()


# 删除tag
@blog_admin.delete("/tag/id/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_id(db, tag_id)
    if not db_tag:
        return status.NotFoundError()

    if db_tag.name == "杂项" or db_tag.name == "默认" or db_tag.name == "default":
        return status.PermissionError(msg="不允许删除!")

    is_success = tag_crud.delete_tag_by_id(db, tag_id)
    if is_success:
        return status.DeleteSuccess()

    return status.DeleteError()


#################################################
# 查询
#################################################

@blog_admin.get("/post/all", response_model=List[schemas.AdminGetPost] | status.QueryError)
def get_draft(db: Session = Depends(get_db)):
    db_posts = post_crud.get_all_post(db)
    if db_posts:
        result = []
        for db_post in db_posts:
            try:
                category = db_post.category.name
            except AttributeError as e:
                category = "默认"

            # 创建 GetPostResponse 对象
            response = schemas.AdminGetPost(
                id=db_post.id,
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


@blog_admin.get("/post/{title}", response_model=schemas.AdminGetPost | status.QueryError)
def get_post_by_title(title: str, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_title(db, title)
    if db_post:
        try:
            category = db_post.category.name
        except AttributeError as e:
            category = "默认"

        resp = schemas.AdminGetPost(
            id=db_post.id,

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


@blog_admin.get("/post/id/{post_id}", response_model=schemas.AdminGetPost | status.QueryError)
def get_post_by_title(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_id(db, post_id)
    if db_post:
        try:
            category = db_post.category.name
        except AttributeError as e:
            category = "默认"

        resp = schemas.AdminGetPost(
            id=db_post.id,

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


@blog_admin.get("/user/all", response_model=List[schemas.AdminGetUser] | list)
def admin_get_all_user(db: Session = Depends(get_db)):
    db_user = user_crud.get_all_user(db)
    if db_user:
        return db_user
    return []


@blog_admin.get("/user/{name}", response_model=schemas.AdminGetUser | status.Base)
def admin_get_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, name)
    if db_user:
        return db_user
    return status.QueryError


@blog_admin.get("/user/id/{user_id}", response_model=schemas.AdminGetUser | status.Base)
def admin_get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user:
        return db_user
    return status.QueryError


@blog_admin.get("/post/id/{post_id}", response_model=schemas.AdminGetPost | status.QueryError)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_id(db, post_id)
    if db_post:
        try:
            category = db_post.category.name
        except AttributeError as e:
            category = "默认"

        resp = schemas.AdminGetPost(
            id=db_post.id,
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


@blog_admin.get("/category/all", response_model=List[schemas.AdminGetCategory] | list)
def get_category_by_id(db: Session = Depends(get_db)):
    db_category = category_crud.get_all_category(db)
    if db_category:
        return db_category
    return []


@blog_admin.get("/category/{name}", response_model=schemas.AdminGetCategory | status.QueryError)
def get_category_by_name(name: str, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_name(db, name)
    if db_category:
        return db_category
    return status.QueryError()


@blog_admin.get("/category/id/{category_id}", response_model=schemas.GetTag | status.QueryError)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = category_crud.get_category_by_id(db, category_id)
    if db_category:
        return db_category
    return status.QueryError()


@blog_admin.get("/tag/all", response_model=List[schemas.AdminGetTag] | list)
def get_tag_by_id(db: Session = Depends(get_db)):
    db_tag = tag_crud.get_all_tag(db)
    if db_tag:
        return db_tag
    return []


@blog_admin.get("/tag/{name}", response_model=schemas.AdminGetTag | status.QueryError)
def get_tag_by_name(name: str, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_name(db, name)
    if db_tag:
        return db_tag
    return status.QueryError()


@blog_admin.get("/tag/id/{tag_id}", response_model=schemas.GetTag | status.QueryError)
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    db_tag = tag_crud.get_tag_by_id(db, tag_id)
    if db_tag:
        return db_tag
    return status.QueryError()


#################################################
# 更新
#################################################

@blog_admin.put(f"/post/id")
def update_post_by_id(post: schemas.AdminUpdatePost, db: Session = Depends(get_db)):
    db_post = post_crud.get_post_by_id(db, post.id)

    if db_post:
        db_category = category_crud.get_category_by_name(db, post.category)
        if not db_category:
            schema_category = schemas.AdminCreateCategory(name=post.category)
            db_category = category_crud.create_category(db, schema_category)
            if not db_category:
                return status.CreateError(msg="新分类创建失败!")

        db_tags = []
        for tag_name in post.tag:
            db_tag = tag_crud.get_tag_by_name(db, tag_name)

            if not db_tag:
                schema_tag = schemas.AdminCreateTag(name=tag_name)
                db_tag = tag_crud.create_tag(db, schema_tag)

            db_tags.append(db_tag)

        db_post.title = post.title
        db_post.content = post.content
        db_post.des = post.des
        db_post.category = db_category
        db_post.tag.clear()
        db_post.tag.extend(db_tags)
        db.add_all([*db_tags])
        db.commit()

        return status.UpdateSuccess()

    return status.UpdateError()


@blog_admin.put(f"/user/id")
def update_post_by_id(user: schemas.AdminUpdateUser, db: Session = Depends(get_db)):
    # 更新后的用户名不能与其他用户的一样
    if user.name:
        db_user_by_name = user_crud.get_user_by_name(db, user.name)
        if db_user_by_name.id != user.id:
            return status.AlreadyExistError(msg="用户名已存在!")

    db_user = user_crud.update_user(db, user)

    if db_user:
        return status.UpdateSuccess()
    return status.UpdateError()


@blog_admin.put(f"/category/id")
def update_category_by_id(category: schemas.AdminUpdateCategory, db: Session = Depends(get_db)):
    db_category = category_crud.update_category(db, category)
    if db_category:
        return status.UpdateSuccess()
    return status.UpdateError()


@blog_admin.put(f"/tag/id")
def update_post_by_id(tag: schemas.AdminUpdateTag, db: Session = Depends(get_db)):
    db_tag = tag_crud.update_tag(db, tag)
    if db_tag:
        return status.UpdateSuccess()
    return status.UpdateError()
