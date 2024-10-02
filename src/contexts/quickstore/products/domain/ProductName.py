class ProductName(object):
    def __init__(
            self, value: str,
    ) -> None:
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._value == other.value
        return False

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: value={self._value!r}>'
