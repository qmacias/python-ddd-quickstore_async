from typing import Callable, Awaitable

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.container import container, config_eventbus

from src.apps.quickstore.backend.routers.users_router import users_router
from src.apps.quickstore.backend.routers.products_router import products_router
from src.apps.quickstore.backend.routers.statuscheck_router import statuscheck_router

from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus

quickstore_backend_app = FastAPI()

quickstore_backend_app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

quickstore_backend_app.include_router(users_router)
quickstore_backend_app.include_router(products_router)
quickstore_backend_app.include_router(statuscheck_router)


@quickstore_backend_app.on_event('startup')
async def startup_event():
    eventbus = container.get(EventBus)

    subscribers_provider = container.get(
        Callable[[], Awaitable[list[EventSubscriber]]]
    )

    subscribers = await subscribers_provider()

    config_eventbus(
        eventbus=eventbus, subscribers=subscribers,
    )
