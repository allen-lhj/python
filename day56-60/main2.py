from fastapi import FastAPI
from typing import Union
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# http://127.0.0.1:8000/items/?skip=0&limit=10 查询参数
# 默认参数
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 可选参数，q是可选的，默认是None
@app.get("/items/{item_id")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return { "item_id": item_id, "q": q }
    return { "item_id": item_id }