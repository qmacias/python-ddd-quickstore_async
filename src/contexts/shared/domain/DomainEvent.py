from uuid import uuid4
from datetime import datetime
from typing import Optional, Any
from abc import ABC, abstractmethod


class DomainEvent(ABC):
    def __init__(
            self,
            event_name: str,
            aggregate_id: str,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ) -> None:
        self._event_name = event_name
        self._aggregate_id = aggregate_id
        self._event_id = event_id or str(uuid4())
        self._occurred_on = occurred_on or datetime.now()

    @abstractmethod
    def to_primitives(self) -> Any:
        pass

    @property
    def event_name(self) -> str:
        return self._event_name

    @property
    def aggregate_id(self) -> str:
        return self._aggregate_id

    @property
    def event_id(self) -> str:
        return self._event_id

    @property
    def occurred_on(self) -> datetime:
        return self._occurred_on

    def __eq__(self, other) -> bool:
        if self.__class__ == other.__class__:
            return self._aggregate_id == other.aggregate_id
        return False
