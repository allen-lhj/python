from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tag: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr = "liu77@qq.com"
    full_name: Union[str, None] = None


@app.post("items/", response_model=Item)
async def create_item(item: Item):
    return item

# Don't do this in production!永远不要存储用户的明文密码，也不要在响应中发送密码。


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# 举个例子，当你在 NoSQL 数据库中保存了具有许多可选属性的模型，但你又不想发送充满默认值的很长的 JSON 响应,你可以设置路径操作装饰器的 response_model_exclude_unset=True 参数

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# 设置路径操作装饰器的 response_model_exclude_unset=True 参数：
# 然后响应中将不会包含那些默认值，而是仅有实际设置的值


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# 还可以使用路径操作装饰器的 response_model_include 和 response_model_exclude 参数。

# 它们接收一个由属性名称 str 组成的 set 来包含（忽略其他的）或者排除（包含其他的）这些属性。

# 如果你只有一个 Pydantic 模型，并且想要从输出中移除一些数据，则可以使用这种快捷方法。


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items[item_id]
