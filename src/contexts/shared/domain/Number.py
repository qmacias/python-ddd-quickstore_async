from random import randint

from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.ValueObject import ValueObject


class Number(ValueObject[int]):
    def __init__(self, value: int) -> None:
        super().__init__(value)

        self.__ensure_valid_number()

    @classmethod
    def random(
            cls,
            min: int = 1,
            max: int = 100,
    ) -> 'Number':
        return cls(randint(min, max))

    def __ensure_valid_number(self) -> None:
        if self._value < 0:
            raise InvalidArgumentError(f'Invalid number: {self._value}')
