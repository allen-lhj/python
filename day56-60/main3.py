from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    # description: Union[str, None] = None
    # price: float
    # tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

# 请求体加路径参数
# fastapi能识别路径参数匹配的函数参数应从路径中取，Pydantic模型的函数参数应从请求体中获取
@app.put("/items/{item_id}")
async def create_items(item_id: int, item: Item):
    return {item}
