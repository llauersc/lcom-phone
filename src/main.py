from typing import Optional

import inject
from fastapi import FastAPI
from redis.asyncio import Redis
from starlette.requests import Request
from starlette.responses import JSONResponse

from models.phones_models import MainException
from services.phones import PhonesService
from routers.phones import router as phones_router
from repositories.phones_repository import PhonesRepository
from settings import Settings

app = FastAPI()
app.include_router(phones_router)


redis: Optional[Redis] = None


def config(binder):
    global redis
    redis = Redis.from_url(Settings.REDIS_URL, encoding="utf-8", decode_responses=True)

    phone_repo = PhonesRepository(redis)
    binder.bind(PhonesRepository, phone_repo)

    service = PhonesService(phone_repo)
    binder.bind(PhonesService, service)


@app.on_event("startup")
async def startup_event():
    inject.configure(config)


@app.on_event("shutdown")
async def shutdown_event():
    global redis
    await redis.close()


@app.exception_handler(MainException)
async def response_exception_handler(request: Request, exc: MainException):
    content = exc.exception_response
    return JSONResponse(status_code=exc.STATUS_CODE, content=content)
