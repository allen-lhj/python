from fastapi import FastAPI
from typing import List, Union

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.put("/items/{item_id}")
async def upate_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
