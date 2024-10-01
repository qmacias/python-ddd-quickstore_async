from abc import ABC, abstractmethod

from src.contexts.shared.domain.DomainEvent import DomainEvent


class EventSubscriber(ABC):
    @abstractmethod
    def subscribed_to(self) -> list[str]:
        pass

    @abstractmethod
    async def on(self, event: DomainEvent) -> None:
        pass
