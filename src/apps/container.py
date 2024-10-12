from typing import Callable, Awaitable

from injector import Module, singleton, provider, Injector
from logging import Logger, getLogger, INFO, Formatter, StreamHandler

from settings import settings
from src.apps.backoffice.backend.deps import BackofficeModule

from src.apps.quickstore.backend.deps import QuickstoreModule, QuickstoreEventSubscribersModule

from tests.contexts.shared.infrastructure.arranger.MongoEnvironmentArranger import MongoEnvironmentArranger
from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger

from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory
from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.infrastructure.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus


class MongoConfigModule(Module):
    @singleton
    @provider
    def config_mongo(self) -> MongoConfig:
        mongoconfig = MongoConfig(uri=settings.MONGODB_URI)

        return mongoconfig


class ArrangerModule(Module):
    @singleton
    @provider
    def environment_arranger(self, config: MongoConfig) -> Callable[[], Awaitable[EnvironmentArranger]]:
        async def __get_environment_arranger() -> EnvironmentArranger:
            client = await MongoClientFactory.create_client('python-ddd-quickstore', config)

            return MongoEnvironmentArranger(client, 'quickstore-backend-dev')

        return __get_environment_arranger


class LoggerModule(Module):
    @singleton
    @provider
    def logger(self) -> Logger:
        return config_logger(__name__)


def config_logger(name: str) -> Logger:
    logger = getLogger(name)

    logger.setLevel(INFO)

    formatter = Formatter(
        '%(levelname)s:%(message)s:%(events)s'
    )

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


class EventBusModule(Module):
    @singleton
    @provider
    def eventbus(self) -> EventBus:
        eventbus = InMemoryEventBus()

        return eventbus


def config_eventbus(
        eventbus: EventBus, subscribers: list[EventSubscriber],
) -> None:
    eventbus.add_subscribers(subscribers)


container = Injector([
    LoggerModule(), EventBusModule(), MongoConfigModule(), ArrangerModule(),
    BackofficeModule(), QuickstoreModule(), QuickstoreEventSubscribersModule()], auto_bind=True,
)
