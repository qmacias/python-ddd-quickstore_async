from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.quickstore.users.domain.UserName import UserName


class UserNameMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'UserName':
        return UserName(value)

    @classmethod
    def random(cls) -> 'UserName':
        return cls.create(cls.get_faker().random_user_name())

    @classmethod
    def invalid(cls) -> 'UserName':
        return cls.create(cls.get_faker().invalid_user_name())
