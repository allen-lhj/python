from typing import Union
from unittest import result

from fastapi import FastAPI, Query, Path

app = FastAPI()

# Query用作查询参数的默认值，并将它的max_length 参数设置为50
# Path为路径参数声明相同类型的校验和元数据
@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"), 
    q: Union[str, None] = Query(default=None, alias="item-query")
):
    results = { "item_id": item_id }
    return results
