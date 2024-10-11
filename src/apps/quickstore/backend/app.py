from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.quickstore.backend.deps import container
from src.apps.quickstore.backend.routers.statuscheck_router import statuscheck_router

from src.contexts.shared.infrastructure.modules.EventBusModule import config_eventbus
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

quickstore_backend_app.include_router(statuscheck_router)


@quickstore_backend_app.on_event('startup')
async def startup_event():
    print('<< QUICKSTORE STARTUP >>')

    # config_eventbus(
    #     eventbus=container.get(EventBus),
    #     subscribers=container.get(list[EventSubscriber]),
    # )
