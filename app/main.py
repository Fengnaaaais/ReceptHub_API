import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.models import Base
from api_v1 import router as api_v1_router


app = FastAPI()
app.include_router(
    router=api_v1_router,
    prefix="/api/v1",
    # tags=["API V1"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
