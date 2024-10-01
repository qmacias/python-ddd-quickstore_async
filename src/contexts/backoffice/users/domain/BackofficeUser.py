from typing import Any, Dict, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.backoffice.users.domain.BackofficeUserId import BackofficeUserId
from src.contexts.backoffice.users.domain.BackofficeUserName import BackofficeUserName
from src.contexts.backoffice.users.domain.BackofficeUserCreated import BackofficeUserCreated


@final
class BackofficeUser(AggregateRoot):
    def __init__(
            self,
            id: BackofficeUserId,
            name: BackofficeUserName,
    ) -> None:
        super().__init__()

        self._id = id
        self._name = name

    @classmethod
    def create(
            cls,
            id: str,
            name: str,
    ) -> 'BackofficeUser':
        user = cls(
            BackofficeUserId(id),
            BackofficeUserName(name),
        )

        user.record(
            BackofficeUserCreated(
                user.id.value, user.name.value,
            )
        )

        return user

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'BackofficeUser':
        return cls(
            BackofficeUserId(plain_data.get('id')),
            BackofficeUserName(plain_data.get('name')),
        )

    @property
    def id(self) -> BackofficeUserId:
        return self._id

    @property
    def name(self) -> BackofficeUserName:
        return self._name

    @name.setter
    def name(self, name: BackofficeUserName) -> None:
        self._name = name  # <-- For duplicator only!

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'id': self._id.value,
            'name': self._name.value,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        attrs: dict = {
            'id': self._id,
            'name': self._name,
        }

        attrs_str: str = ', '.join(
            f'{k}={v!r}' for k, v in attrs.items()
        )

        return f'<{self.__class__.__name__}: {attrs_str}>'
