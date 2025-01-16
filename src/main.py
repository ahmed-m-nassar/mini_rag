from fastapi import FastAPI
from routes import base, data
from helpers.config import get_settings


app = FastAPI()

async def startup_span():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]


async def shutdown_span():
    app.mongo_conn.close()

app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
