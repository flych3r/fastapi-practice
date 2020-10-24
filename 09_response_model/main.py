from typing import List, Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseItem(BaseModel):
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car",
        "price": 50.2
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "price": 20.2,
        "type": "plane",
        "size": 5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Union[PlaneItem, CarItem],
    response_model_include={"type", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get(
    "/items/{item_id}/public",
    response_model=Union[PlaneItem, CarItem],
    response_model_exclude={"tax"}
)
async def read_item_public_data(item_id: str):
    return items[item_id]


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
