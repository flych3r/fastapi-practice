from typing import List, Optional

from fastapi import Cookie, Header, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


@app.get("/users/")
async def read_user(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}
