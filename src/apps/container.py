from typing import Callable, Awaitable

from logging import Logger, getLogger, INFO, Formatter, StreamHandler
from injector import Module, singleton, provider, Injector, multiprovider, inject

from settings import settings

from src.apps.backoffice.backend.deps import BackofficeModule
from src.contexts.backoffice.users.application.create.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.application.create.CreateBackofficeUserOnUserCreated import CreateBackofficeUserOnUserCreated

from src.apps.quickstore.backend.deps import QuickstoreModule
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.application.create.CreateProductOnBackofficeProductCreated import CreateProductOnBackofficeProductCreated

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
        eventbus: EventBus,
        subscribers: list[EventSubscriber],
) -> None:
    eventbus.add_subscribers(subscribers)


class EventSubscribersModule(Module):
    @singleton
    @multiprovider
    @inject
    def event_subscribers(
            self,
            backoffice_user_creator_provider: Callable[[], Awaitable[BackofficeUserCreator]],
            quickstore_product_creator_provider: Callable[[], Awaitable[ProductCreator]],
    ) -> Callable[[], Awaitable[list[EventSubscriber]]]:
        async def __get_event_subscribers() -> list[EventSubscriber]:
            backoffice_user_creator = await backoffice_user_creator_provider()
            quickstore_product_creator = await quickstore_product_creator_provider()

            return [
                CreateBackofficeUserOnUserCreated(backoffice_user_creator),
                CreateProductOnBackofficeProductCreated(quickstore_product_creator),
            ]

        return __get_event_subscribers


container = Injector([
    LoggerModule(), EventBusModule(),
    MongoConfigModule(), ArrangerModule(),
    BackofficeModule(), QuickstoreModule(), EventSubscribersModule()], auto_bind=True,
)
