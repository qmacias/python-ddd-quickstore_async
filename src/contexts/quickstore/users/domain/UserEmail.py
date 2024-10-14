from re import compile

from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.ValueObject import ValueObject


class UserEmail(ValueObject[str]):
    """
    The email must adhere to the following rules:
        - It must contain a local part, followed by an '@' symbol, then a domain name.
        - The local part can contain letters (a-z, A-Z), numbers (0-9), and the characters '.', '_', '+', and '-'.
        - The domain part must contain a domain name followed by a top-level domain (TLD).
        - The domain name can contain letters, numbers, and hyphens.
        - The TLD must contain at least one period followed by letters or numbers.

    Explanation of the regex:
        - '^': Start of the string
        - '[a-zA-Z0-9_.+-]+': One or more characters from the set (letters, numbers, '.', '_', '+', '-')
        - '@': Literal '@' symbol
        - '[a-zA-Z0-9-]+': One or more characters from the set (letters, numbers, '-')
        - '\\.': Literal '.' (escaped with backslash)
        - '[a-zA-Z0-9-.]+': One or more characters from the set (letters, numbers, '-', '.')
        - '$': End of the string
    """
    __REGEX = compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    def __init__(
            self, value: str,
    ) -> None:
        super().__init__(value)

        self.__ensure_valid_email()

    def __ensure_valid_email(self) -> None:
        if not self.__REGEX.match(self._value):
            raise InvalidArgumentError(f'Invalid email: {self._value!r}')
