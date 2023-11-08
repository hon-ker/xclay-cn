#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from pydantic import BaseModel, EmailStr
from typing import Optional


# 数据规范
class Base(BaseModel):
    class Config:
        orm_mode = True


class GetPost(Base):
    title: str
    content: str
    des: str = "暂无描述……"
    tag: list
    category: str
    user: str
    ctime: Optional[str]
    ltime: Optional[str]


class AdminGetPost(GetPost):
    id: int


class AdminCreatePost(GetPost):
    pass


class AdminUpdatePost(Base):
    id: int
    title: Optional[str] = None
    content: Optional[str] = None
    des: Optional[str] = None
    tag: Optional[list] = None
    category: Optional[str] = None
    ctime: Optional[str] = None
    ltime: Optional[str] = None


class GetTag(Base):
    name: str
    des: str


class AdminGetTag(GetTag):
    id: int


class AdminCreateTag(Base):
    name: Optional[str]
    des: Optional[str] = "暂无描述……"


class AdminUpdateTag(AdminCreateTag):
    id: int
    name: Optional[str] = None
    des: Optional[str] = None


class GetCategory(GetTag):
    pass


class AdminGetCategory(GetTag):
    id: int


class AdminCreateCategory(GetTag):
    pass


class AdminUpdateCategory(AdminUpdateTag):
    pass


class Login(Base):
    name: str
    passwd: str
    token: Optional[str] | None = None


class Register(Base):
    name: str
    passwd: str
    des: Optional[str] = None
    avatar: Optional[str] = None
    mail: Optional[EmailStr] = None
    is_manager: Optional[bool] = False
    is_token_valid: Optional[bool] = True
    token: Optional[str] = None


class GetUser(Base):
    name: str
    des: Optional[str]
    avatar: Optional[str]


class UpdateUser(Base):
    id: int
    name: Optional[str] = None
    des: Optional[str] = None
    mail: Optional[EmailStr] = None
    avatar: Optional[str] = None
    passwd: Optional[str] = None
    token: Optional[str] = None


class SelfGetUser(UpdateUser):
    pass


class AdminGetUser(Base):
    id: int
    name: str
    des: Optional[str] = None
    mail: Optional[EmailStr] = None
    avatar: Optional[str] = None
    is_token_valid: Optional[bool] = None
    is_manager: Optional[bool] = None
    token: Optional[str] = None


class AdminCreateUser(Register):
    pass


class AdminUpdateUser(UpdateUser):
    is_token_valid: Optional[bool] = None
    is_manager: Optional[bool] = None
