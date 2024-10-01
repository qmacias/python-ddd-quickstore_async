from datetime import datetime
from typing import Any, Dict, Optional, final

from src.contexts.shared.domain.DomainEvent import DomainEvent


@final
class BackofficeUserCreated(DomainEvent):
    EVENT_TYPE = 'backoffice.user.created'

    def __init__(
            self,
            aggregate_id: str,
            name: str,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ) -> None:
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)

        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def to_primitives(self) -> Dict[Any, Any]:
        return {
            'data': {
                'eventId': self._event_id,
                'type': self.EVENT_TYPE,
                'occurred_on': str(self._occurred_on),
                'aggregateId': self._aggregate_id,
                'attributes': {
                    'name': self._name,
                },
            },
            'meta': {
                'attempts': 0,
            }
        }
