#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from fastapi import Cookie, FastAPI, Depends, Depends, HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from hashlib import md5

from blog import schemas
from utils import status, exceptions
import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 创建jwt token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    # 令牌过期时间
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 没传入就传入30分钟
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=config.SECRET_KEY, algorithm=config.ALGORITHM)

    return encoded_jwt


def get_decoded_token(token: str = Cookie(default="token")):
    if token is None:
        raise HTTPException(status_code=401)
    try:
        decoded_token = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.ALGORITHM])
        return decoded_token
    except JWTError as e:
        print(e.args[0])
        # 如果令牌已经过期，可以在这里进行适当的处理
        # 例如：返回错误信息或自动刷新令牌等
        raise HTTPException(status_code=401, detail="登录已过期，请重新登录!")


# 判断是不是登录，如果是返回解码后的token
def check_login(token: str = Cookie(default=None)):
    token = get_decoded_token(token)
    if token:
        return token
    return False


# 判断是不是登录，如果是返回解码后的token
def check_manager(token: str = Cookie(default=None)):
    token = get_decoded_token(token)
    if token.get("is_manager"):
        return token
    return False
