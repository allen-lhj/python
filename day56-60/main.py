from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# 路径参数，
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 路径顺序

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
# /users/me的路径需要在/users/{user_id}前面，否则 /users/{user_id}会先与/users/me匹配，
# 认为自己正在接收一个值为“me” 的user_id 参数
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": "user_id"}

# 基于baseModel 定义请求体结构(json 对象)

class LoginUser(BaseModel):
    phone: str
    code: str


@app.post("/login")
def user_login(user: LoginUser):
    # 查询phone是否存在
    # 验证code 是否有效
    return {'msg': '用户已登录', 'phone': user.phone}
