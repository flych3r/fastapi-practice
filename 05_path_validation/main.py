from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q, "size": size})
    return results
