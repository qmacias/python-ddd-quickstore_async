from re import compile

from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.ValueObject import ValueObject


class BackofficeProductName(ValueObject[str]):
    """
    The name must adhere to the following rules:
        - Must consist of two or more words.
        - Each word must start with an uppercase letter.
        - The rest of each word must be in lowercase.
        - The words must be separated by single spaces.

    Explanation of the regex:
        - '^': Start of the string
        - '([A-Z][a-z]+)': First name (uppercase first letter, rest lowercase)
        - '((\s[A-Z][a-z]+)+)': One or more additional names, each preceded by a space
        - '$': End of the string
    """
    __REGEX = compile(r'^([A-Z][a-z]+)((\s[A-Z][a-z]+)+)$')

    def __init__(
            self, value: str,
    ) -> None:
        super().__init__(value)

        self.__ensure_valid_name()

    def __ensure_valid_name(self) -> None:
        if not self.__REGEX.match(self._value):
            raise InvalidArgumentError(f'Invalid name: {self._value!r}')
