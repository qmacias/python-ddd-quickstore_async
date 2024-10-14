from tests.contexts.shared.domain.Uuid4Mother import Uuid4Mother

from src.contexts.quickstore.users.domain.UserId import UserId


class UserIdMother:
    @staticmethod
    def create(
            value: str,
    ) -> 'UserId':
        return UserId(value)

    @classmethod
    def random(cls) -> 'UserId':
        return cls.create(Uuid4Mother.random())

    @classmethod
    def invalid(cls) -> 'UserId':
        return cls.create(cls.random().value + '.')
