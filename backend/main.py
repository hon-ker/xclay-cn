#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 入口文件

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from typing import Annotated

from blog import blog_ordinary, blog_admin
from blog import auth
from other import other_app
from test import test_app

app = FastAPI(
    title='Xclay博客',
    description='Fastapi博客系统',
    version='1.0.0',
    docs_url='/',
    redoc_url='/redocs',
)
origin = [
    "http://localhost:5173"
]
# 添加中间件
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount表示将某个目录下一个完全独立的应用挂载过来，这个不会在API交互文档中显示
app.mount(path='/static', app=StaticFiles(directory='./static'),
          name='static')  # .mount()不要在分路由APIRouter().mount()调用，模板会报错

app.include_router(test_app, prefix='/test', tags=['测试API'])
app.include_router(blog_ordinary, prefix='/api', tags=['普通用户API'])
app.include_router(blog_admin, prefix='/api/admin', tags=['管理员API'], dependencies=[])
# app.include_router(blog_admin, prefix='/api/admin', tags=['管理员API'], dependencies=[Depends(auth.check_login)])
app.include_router(other_app, prefix='', tags=['其他API'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
