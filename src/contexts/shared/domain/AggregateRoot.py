from abc import ABC, abstractmethod
from typing import Dict, Any

from src.contexts.shared.domain.DomainEvent import DomainEvent


class AggregateRoot(ABC):
    def __init__(self) -> None:
        self.__events: list[DomainEvent] = []

    def pull_domain_events(self) -> list[DomainEvent]:
        events = self.__events[:]
        self.__events = []

        return events

    def record(self, event: DomainEvent) -> None:
        self.__events.append(event)

    @abstractmethod
    def to_primitives(self) -> Dict[str, Any]:
        pass
