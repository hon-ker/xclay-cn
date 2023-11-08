#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from fastapi import HTTPException, status


def exception(status_code: int = status.HTTP_401_UNAUTHORIZED, msg: str = "请先登录!"):
    return HTTPException(status_code=status_code, detail=msg)


# 认证错误
AuthorizedError = exception()
# 权限不足
PermissionError = exception(status.HTTP_403_FORBIDDEN, "权限不足!")
