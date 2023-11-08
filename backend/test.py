import json
from fastapi import APIRouter, Cookie
from fastapi.responses import JSONResponse
from blog import auth
from utils import status

test_app = APIRouter()


@test_app.get("/set_cookie")
async def set_cookie():
    access_token = auth.create_access_token(data={"name": "假欢", "is_manager": True})
    response = JSONResponse(content={"token": access_token})
    # response = JSONResponse(content=status.ActionSuccess(msg="登录成功!").dict())
    response.set_cookie(key="token", value=access_token, httponly=True)  # 将token设置为httponly的cookie
    return response


@test_app.get("/get_cookie")
async def set_cookie(token: str = Cookie(default="token")):
    return {"token": token}
