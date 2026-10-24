from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.router import api_router as auth_app_router
from src.constants.errors import DomainError
from src.utils.errors import domain_error_exception_handler


app = FastAPI(
    title="MatrixApp",
    openapi_url="/matrix/openapi.json",
    docs_url="/matrix/docs",
    exception_handlers={DomainError: domain_error_exception_handler},


)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_app_router, prefix="/matrix")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
    )