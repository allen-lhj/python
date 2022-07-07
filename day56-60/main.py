from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 基于baseModel 定义请求体结构(json 对象)


class LoginUser(BaseModel):
    phone: str
    code: str


@app.post("/login")
def user_login(user: LoginUser):
    # 查询phone是否存在
    # 验证code 是否有效
    return {'msg': '用户已登录', 'phone': user.phone}
