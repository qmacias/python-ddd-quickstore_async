from decimal import Decimal
from datetime import datetime

from abc import ABC
from typing import TypeVar, Generic

Primitives = str | int | float | bool | bytes | Decimal | datetime

T = TypeVar('T', bound=Primitives)


class ValueObject(Generic[T], ABC):
    def __init__(self, value: T) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(
            self, other: 'ValueObject[T]',
    ) -> bool:
        if self.__class__ == other.__class__:
            return self._value == other.value
        return False

    def __int__(self) -> int:
        return int(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: value={self._value!r}>'
