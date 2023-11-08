#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from typing import Optional
from pydantic import BaseModel


class Base(BaseModel):
    status_code: int
    msg: str
    redirect: Optional[str] = None


class NotFoundError(Base):
    status_code: int = 404
    msg: str = "未找到!"
    redirect: Optional[str] = None


class AlreadyExistError(Base):
    status_code: int = 400
    msg: str = "已存在!"


class CreateSuccess(Base):
    status_code: int = 200
    msg: str = "创建成功!"


class DeleteSuccess(Base):
    status_code: int = 200
    msg: str = "删除成功!"


class UpdateSuccess(Base):
    status_code: int = 200
    msg: str = "更新成功!"


class QuerySuccess(Base):
    status_code: int = 400
    msg: str = "获取失败!"


class ActionSuccess(Base):
    status_code: int = 200
    msg: str = "执行成功!"


class CreateError(Base):
    status_code: int = 400
    msg: str = "创建失败!"


class DeleteError(Base):
    status_code: int = 400
    msg: str = "删除失败!"


class UpdateError(Base):
    status_code: int = 400
    msg: str = "更新失败!"


class QueryError(Base):
    status_code: int = 400
    msg: str = "获取失败!"


class PermissionError(Base):
    status_code: int = 400
    msg: str = "无权操作!"


class ActionError(Base):
    status_code: int = 400
    msg: str = "操作失败!"
