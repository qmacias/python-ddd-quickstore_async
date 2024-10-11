from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.backoffice.backend.deps import backoffice_container
from src.apps.backoffice.backend.routers.users_router import users_router
from src.apps.backoffice.backend.routers.products_router import products_router
from src.apps.backoffice.backend.routers.statuscheck_router import statuscheck_router

from src.contexts.shared.infrastructure.modules.EventBusModule import config_eventbus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus

backoffice_backend_app = FastAPI()

backoffice_backend_app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

backoffice_backend_app.include_router(users_router)
backoffice_backend_app.include_router(products_router)
backoffice_backend_app.include_router(statuscheck_router)


@backoffice_backend_app.on_event('startup')
async def startup_event():
    print('<< BACKOFFICE STARTUP >>')

    # config_eventbus(
    #     eventbus=backoffice_container.get(EventBus),
    #     subscribers=backoffice_container.get(list[EventSubscriber]),
    # )
