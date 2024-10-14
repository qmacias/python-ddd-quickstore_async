from tests.contexts.shared.domain.MotherCreator import MotherCreator

from src.contexts.quickstore.users.domain.UserEmail import UserEmail


class UserEmailMother(MotherCreator):
    @staticmethod
    def create(
            value: str,
    ) -> 'UserEmail':
        return UserEmail(value)

    @classmethod
    def random(cls) -> 'UserEmail':
        return cls.create(cls.get_faker().random_user_email())

    @classmethod
    def invalid(cls) -> 'UserEmail':
        return cls.create(cls.get_faker().invalid_user_email())
