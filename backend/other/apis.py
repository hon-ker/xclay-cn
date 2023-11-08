#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

# 博客的apis
from typing import List, Optional, Union
from fastapi import APIRouter, Response, UploadFile
from datetime import datetime
import random
import os

from utils import status

other_app = APIRouter()


# gif
@other_app.get("/other/gif")
def get_gif():
    gifs = os.listdir("static/gif/")
    url = "/static/gif/" + random.choice(gifs)
    return {"url": url}


# 图片上传
@other_app.post('/img/upload')
async def upload_image(file: UploadFile):
    contents = await file.read()  # 读取文件内容
    filename, ext = os.path.splitext(file.filename)

    if ext in [".png", ".jpg", ".gif"]:
        now = datetime.now()
        save_path = f"static/upload/{now.year}/{now.month}/{now.day}/{filename}{ext}"

        # 处理文件名重复的策略
        i = 1
        while os.path.exists(save_path):
            save_path = f"static/upload/{now.year}/{now.month}/{now.day}/{filename}_{i}{ext}"
            i += 1

        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as f:
            f.write(contents)  # 将文件内容写入到服务器指定目录

        return {"name": filename, "url": f"/{save_path}"}

    return status.PermissionError()
