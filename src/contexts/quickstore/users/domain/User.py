from typing import Any, Dict, final

from src.contexts.shared.domain.AggregateRoot import AggregateRoot

from src.contexts.quickstore.users.domain.UserId import UserId
from src.contexts.quickstore.users.domain.UserName import UserName
from src.contexts.quickstore.users.domain.UserEmail import UserEmail
from src.contexts.quickstore.users.domain.UserCreated import UserCreated


@final
class User(AggregateRoot):
    def __init__(
            self,
            id: UserId,
            name: UserName,
            email: UserEmail,
    ) -> None:
        super().__init__()

        self._id = id
        self._name = name
        self._email = email

    @classmethod
    def create(
            cls,
            id: str,
            name: str,
            email: str,
    ) -> 'User':
        user = cls(
            UserId(id),
            UserName(name),
            UserEmail(email),
        )

        user.record(
            UserCreated(
                user.id.value, user.name.value, user.email.value,
            )
        )

        return user

    @classmethod
    def from_primitives(
            cls, plain_data: Any,
    ) -> 'User':
        return cls(
            UserId(plain_data.get('id')),
            UserName(plain_data.get('name')),
            UserEmail(plain_data.get('email')),
        )

    @property
    def id(self) -> UserId:
        return self._id

    @property
    def name(self) -> UserName:
        return self._name

    @property
    def email(self) -> UserEmail:
        return self._email

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'id': self._id.value,
            'name': self._name.value,
            'email': self._email.value,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        attrs: dict = {
            'id': self._id,
            'name': self._name,
            'email': self._email,
        }

        attrs_str: str = ', '.join(
            f'{k}={v!r}' for k, v in attrs.items()
        )

        return f'<{self.__class__.__name__}: {attrs_str}>'
