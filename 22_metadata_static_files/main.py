from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="My Super Project",
    description="This is a very fancy project,"
    " with auto docs for the API and everything",
    version="2.5.0",
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    docs_url="/documentation",
    redoc_url=None
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
