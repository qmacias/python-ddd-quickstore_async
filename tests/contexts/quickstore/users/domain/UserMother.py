from src.contexts.quickstore.users.domain.User import User

from tests.contexts.quickstore.users.domain.UserIdMother import UserIdMother
from tests.contexts.quickstore.users.domain.UserNameMother import UserNameMother
from tests.contexts.quickstore.users.domain.UserEmailMother import UserEmailMother


class UserMother:
    @staticmethod
    def create(
            id: str,
            name: str,
            email: str,
    ) -> 'User':
        return User.create(
            UserIdMother.create(id).value,
            UserNameMother.create(name).value,
            UserEmailMother.create(email).value,
        )

    @classmethod
    def random(cls) -> 'User':
        return cls.create(
            UserIdMother.random().value,
            UserNameMother.random().value,
            UserEmailMother.random().value,
        )

    @staticmethod
    def create_without_events(
            id: str,
            name: str,
            email: str,
    ) -> 'User':
        return User(
            UserIdMother.create(id),
            UserNameMother.create(name),
            UserEmailMother.create(email),
        )

    @staticmethod
    def random_without_events() -> 'User':
        return User(
            UserIdMother.random(),
            UserNameMother.random(),
            UserEmailMother.random(),
        )

    @classmethod
    def with_bad_id(cls) -> 'User':
        return cls.create(
            UserIdMother.invalid().value,
            UserNameMother.random().value,
            UserEmailMother.random().value,
        )

    @classmethod
    def with_bad_name(cls) -> 'User':
        return cls.create(
            UserIdMother.random().value,
            UserNameMother.invalid().value,
            UserEmailMother.random().value,
        )

    @classmethod
    def with_bad_email(cls) -> 'User':
        return cls.create(
            UserIdMother.random().value,
            UserNameMother.random().value,
            UserEmailMother.invalid().value,
        )
