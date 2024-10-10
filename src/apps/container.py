from injector import Module, singleton, provider, Injector
from logging import Logger, getLogger, INFO, Formatter, StreamHandler

from settings import settings

from src.apps.backoffice.backend.deps import BackofficeModule

from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.infrastructure.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus


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
    def event_bus(self) -> EventBus:
        event_bus = InMemoryEventBus()

        return event_bus


def configure_event_bus(
        event_bus: EventBus, subscribers: list[EventSubscriber],
) -> None:
    event_bus.add_subscribers(subscribers)


class MongoConfigModule(Module):
    @singleton
    @provider
    def config(self) -> MongoConfig:
        config = MongoConfig(uri=settings.MONGODB_URI)

        return config


container = Injector(
    [
        LoggerModule(), EventBusModule(),
        MongoConfigModule, BackofficeModule(),
    ], auto_bind=True
)

# configure_event_bus(event_bus=container.get(EventBus), subscribers=container.get(list[EventSubscriber]))
