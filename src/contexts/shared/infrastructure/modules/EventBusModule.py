from injector import Module, singleton, provider

from src.contexts.shared.infrastructure.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus


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


eventbus = EventBusModule()
