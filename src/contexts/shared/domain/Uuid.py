from uuid import UUID, uuid4

from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.ValueObject import ValueObject


class Uuid(ValueObject[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value)

        self.__ensure_valid_uuid()

    @classmethod
    def random(cls) -> 'Uuid':
        return cls(str(uuid4()))

    def __ensure_valid_uuid(self) -> None:
        try:
            UUID(self._value, version=4)
        except ValueError as e:
            raise InvalidArgumentError(f'Invalid id: {self._value!r}') from e
