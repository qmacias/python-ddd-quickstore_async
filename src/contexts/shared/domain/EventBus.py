from abc import ABC, abstractmethod

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventSubscriber import EventSubscriber


class EventBus(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        pass

    @abstractmethod
    def add_subscribers(self, subscribers: list[EventSubscriber]) -> None:
        pass
