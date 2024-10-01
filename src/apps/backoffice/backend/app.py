from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.backoffice.backend.routers.statuscheck_router import statuscheck_router
from src.apps.backoffice.backend.routers.users_router import users_router

backoffice_backend_app = FastAPI()

backoffice_backend_app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

backoffice_backend_app.include_router(statuscheck_router)
backoffice_backend_app.include_router(users_router)
