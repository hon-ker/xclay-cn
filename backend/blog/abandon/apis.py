#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from typing import List, Optional, Union
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request, status, UploadFile
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from blog.db import engine, Base, SessionLocal
from blog import models, schemas, crud
from utils.log import log
from utils.tools import upload_file

blog = APIRouter()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 新建文章
@blog.post("/create/post", response_model=schemas.RespMsg)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_title(db, title=post.title)
    if db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该文章已存在!")

    # 创建基础post
    db_post = models.Post(title=post.title, content=post.content, cover=post.cover, des=post.des, view=0, star=0)

    # 用户查询
    db_user = crud.get_user(db, post.user)
    # 用户不存在？

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"无效用户!")
    # 用户不是管理员
    if not db_user.is_manager:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户没有权限!")

    # 创建tag
    db_tags = []
    for tag_name in post.tag:
        tag_obj = schemas.CreateTag(name=tag_name)
        tag = crud.get_tag_by_name(db, tag_name)
        if not tag:
            tag = crud.create_tag(db, tag_obj)
        db_tags.append(tag)

    # 查询category
    db_category = crud.get_category_by_name(db, post.category)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该分类不存在!")

    db_cover = ""
    if post.cover:
        cover = upload_file(post.cover, allowed_type=["jpg", "jpeg", "gif", "gif"])
        db_cover = cover.get("src", "")

    # 封面
    db_post.cover = db_cover
    # 分类
    db_post.category = db_category
    db_post.category_id = db_category.id
    # 标签
    db_post.tag.extend(db_tags)
    # 作者
    db_post.user = db_user
    db_post.user_id = db_user.id

    # 提交数据
    db.add_all([*db_tags, db_post])
    db.commit()

    return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}


# 新建分类
@blog.post("/create/category", response_model=schemas.RespMsg)
def create_category(category: schemas.CreateCategory, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail=f"该分类已存在!")

    is_success = crud.create_category(db, category)
    if is_success:
        return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}

    return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}


# 新建分类
@blog.post("/create/tag", response_model=schemas.RespMsg)
def create_tag(tag: schemas.CreateTag, db: Session = Depends(get_db)):
    db_tag = crud.get_tag_by_name(db, tag.name)
    if db_tag:
        raise HTTPException(status_code=400, detail=f"该标签已存在!")
    is_success = crud.create_tag(db, tag)
    if is_success:
        return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}

    return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}


# 新建用户
@blog.post("/create/user", response_model=schemas.RespMsg)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.name)
    if db_user:
        raise HTTPException(status_code=400, detail=f"该用户已存在!")

    is_success = crud.create_user(db, user)
    if is_success:
        return {"status_code": status.HTTP_200_OK, "msg": "创建成功!"}


# 回收文章
@blog.delete("/delete/post", response_model=schemas.RespMsg)
def recycle_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_title(db, title=post.title)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该文章不存在!")
    else:
        db_post.is_active = False
        db.commit()
        return {"status_code": status.HTTP_200_OK, "msg": "回收成功!"}


# 删除文章
@blog.delete("/delete/post", response_model=schemas.RespMsg)
def delete_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_title(db, title=post.title)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该文章不存在!")
    else:
        db_post.delete()
        db.commit()
        return {"status_code": status.HTTP_200_OK, "msg": "删除成功!"}


# 删除tag
@blog.delete("/delete/tag", response_model=schemas.RespMsg)
def delete_tag(tag: schemas.CreateTag, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_tag = crud.get_tag_by_name(db, tag.name)
    if not db_tag:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该标签不存在!")
    else:
        db_tag.delete()
        db.commit()
        return {"status_code": status.HTTP_200_OK, "msg": "删除成功!"}


# 删除category
@blog.delete("/delete/category", response_model=schemas.RespMsg)
def delete_category(category: schemas.CreateCategory, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_category = crud.get_category_by_name(db, category.name)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该分类不存在!")
    else:
        db_category.delete()
        db.commit()
        return {"status_code": status.HTTP_200_OK, "msg": "删除成功!"}


# 删除user
@blog.delete("/delete/user", response_model=schemas.RespMsg)
def delete_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_user = crud.is_user(db, user)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        db_user.delete()
        db.commit()
        return {"status_code": status.HTTP_200_OK, "msg": "删除成功!"}


# 获取post 通过title
# @blog.get("/post")
@blog.get("/post", response_model=List[schemas.GetPost])
def get_post(db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post(db)

    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        result = []
        for item in db_post:
            # 创建 GetPostResponse 对象
            response = schemas.GetPost(
                title=item.title,
                content=item.content,
                tag=[tag.name for tag in item.tag],
                category=item.category.name,
                user=item.user.name,
                des=item.des,
                cover=item.cover,
                view=item.view,
                star=item.star,
                ctime=str(item.ctime),
                ltime=str(item.ltime)

            )

            result.append(response)
        return result


# 获取tag列表
@blog.get("/tag", response_model=List[schemas.GetTag])
def get_tag(db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_tag = crud.get_tag(db)
    if not db_tag:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_tag


# 获取category列表
@blog.get("/category", response_model=List[schemas.GetCategory])
def get_category(db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_category = crud.get_category(db)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_category


# 获取draft 通过title
@blog.get("/crud/{title}", response_model=schemas.GetDraft)
def get_draft(title: str, db: Session = Depends(get_db)):
    db_draft = crud.get_draft_by_title(db, title)
    if not db_draft:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    return db_draft


# 获取draft 通过title
@blog.get("/crud", response_model=List[schemas.GetDraft])
def get_draft(db: Session = Depends(get_db)):
    db_draft = crud.get_draft(db)
    if not db_draft:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    return db_draft


@blog.get("/post/{title}", response_model=schemas.GetPost)
def get_post(title: str, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_title(db, title)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        log.succes(db_post.content)
        return schemas.GetPost(
            title=db_post.title,
            content=db_post.content,
            tag=[tag.name for tag in db_post.tag],
            category=db_post.category.name,
            user=db_post.user.name,
            des=db_post.des,
            cover=db_post.cover,
            view=db_post.view,
            star=db_post.star,
            ctime=str(db_post.ctime),
            ltime=str(db_post.ltime)
        )


# 获取post 通过user
@blog.get("/post/{user}", response_model=List[schemas.GetPost])
def get_user_post(user: str, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_user(db, user)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_post


# 获取post列表 通过tag
@blog.get("/post/{tag}", response_model=List[schemas.GetPost])
def get_tag_post(tag: str, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_tag(db, tag)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_post


# 获取post列表 通过category
@blog.get("/post/{category}", response_model=List[schemas.GetPost])
def get_category_post(category: str, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_post = crud.get_post_by_category(db, category)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_post


# 获取文章
@blog.get("/user", response_model=List[schemas.GetUser])
def get_all_user(db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_user = crud.get_all_user(db)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_user


# 获取文章
@blog.get("/user/{name}", response_model=schemas.GetUser)
def get_user(name: str, db: Session = Depends(get_db)):
    # 判断文章是否存在
    db_user = crud.get_user(db, name)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户不存在!")
    else:
        return db_user


@blog.put("/update/crud", response_model=schemas.RespMsg)
def update_draft(id: int, db: Session = Depends(get_db)):
    db_draft = crud.get_draft_by_id(db, id)
    if not db_draft:
        raise HTTPException(status_code=400, detail=f"无效标签!")

    db.commit()
    return {"status_code": status.HTTP_200_OK, "msg": "更新成功!"}


# 修改文章
@blog.put("/update/post", response_model=schemas.RespMsg)
def update_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    db_post = crud.get_post_by_title(db, post.title)
    if not db_post:
        raise HTTPException(status_code=400, detail=f"该文章不存在!")

    # 用户查询
    db_user = crud.get_user(db, post.user)
    # 用户不存在？
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"无效用户!")
    # 用户不是管理员
    if not db_user.is_manager:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该用户没有权限!")

    # 创建tag
    db_tags = []
    for tag_name in post.tag:
        tag_obj = schemas.CreateTag(name=tag_name)
        tag = crud.get_tag_by_name(db, tag_name)
        if not tag:
            tag = crud.create_tag(db, tag_obj)
        db_tags.append(tag)

    # 查询category
    db_category = crud.get_category_by_name(db, post.category)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"该分类不存在!")

    # 设置post其他属性
    # 分类
    db_post.category = db_category
    db_post.category_id = db_category.id
    # 标签
    db_post.tag.extend(db_tags)
    # 作者
    db_post.user = db_user
    db_post.user_id = db_user.id

    db.commit()
    return {"status_code": status.HTTP_200_OK, "msg": "更新成功!"}


# 修改tag
@blog.put("/update/tag", response_model=schemas.RespMsg)
def update_tag(tag: schemas.CreateTag, db: Session = Depends(get_db)):
    db_tag = crud.get_tag_by_name(db, tag.name)
    if not db_tag:
        raise HTTPException(status_code=400, detail=f"无效标签!")

    db_tag.des = tag.des
    db.commit()
    return {"status_code": status.HTTP_200_OK, "msg": "更新成功!"}


# 修改category
@blog.put("/update/category", response_model=schemas.RespMsg)
def update_category(category: schemas.CreateTag, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, category.name)
    if not db_category:
        raise HTTPException(status_code=400, detail=f"无效分类!")

    db_category.des = category.des
    db.commit()
    return {"status_code": status.HTTP_200_OK, "msg": "更新成功!"}


# 修改用户权限
@blog.put("/update/user", response_model=schemas.RespMsg)
def update_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.name)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"无效用户!")

    db_user.name = user.name
    db_user.passwd = user.passwd
    db_user.avatar = user.avatar
    db_user.is_manager = user.is_manager
    db.commit()
    return {"status_code": status.HTTP_200_OK, "msg": "更新成功!"}


@blog.post("/upload", response_model=schemas.RespFile)
async def upload(file: UploadFile) -> schemas.RespFile:
    contents = await file.read()  # 读取文件内容
    src = "static/upload/" + file.filename
    with open(src, 'wb') as f:
        f.write(contents)  # 将文件内容写入到服务器指定目录
    return schemas.RespFile(alt=os.path.splitext(file.filename)[0], src="/" + src)
