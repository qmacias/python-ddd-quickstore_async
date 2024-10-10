from injector import Module, singleton, provider

from src.contexts.shared.infrastructure.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.EventBus import EventBus


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
