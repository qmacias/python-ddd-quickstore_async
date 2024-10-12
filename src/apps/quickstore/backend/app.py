from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.quickstore.backend.routers.statuscheck_router import statuscheck_router

quickstore_backend_app = FastAPI()

quickstore_backend_app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

quickstore_backend_app.include_router(statuscheck_router)
