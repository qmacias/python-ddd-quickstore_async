from logging import Logger

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.quickstore.users.application.UserCreator import UserCreator
from src.contexts.quickstore.users.domain.UserRepository import UserRepository
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.EventBus import EventBus

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.shared.domain.users.UserEmailProvider import UserEmailProvider
from tests.contexts.quickstore.users.domain.UserMother import UserMother
from tests.contexts.quickstore.users.domain.UserCreatedMother import UserCreatedMother


class UserCreatorTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        MotherCreator.add_provider(UserNameProvider)
        MotherCreator.add_provider(UserEmailProvider)

        self.__eventbus = AsyncMock(spec=EventBus)
        self.__repository = AsyncMock(spec=UserRepository)

        self.__creator = (
            UserCreator(self.__repository, self.__eventbus, AsyncMock(spec=Logger))
        )

    async def test_should_create_a_valid_user(self) -> None:
        user = UserMother.random()

        domain_events = [
            UserCreatedMother.create(
                user.id.value, user.name.value, user.email.value,
            )
        ]

        await self.__creator(user.id.value, user.name.value, user.email.value)

        self.__repository.save.assert_called_once_with(user)
        self.__eventbus.publish.assert_called_once_with(domain_events)

    async def test_should_not_create_an_invalid_user_with_bad_id(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            user = UserMother.with_bad_id()

            await self.__creator(user.id.value, user.name.value, user.email.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_user_with_bad_name(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            user = UserMother.with_bad_name()

            await self.__creator(user.id.value, user.name.value, user.email.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_user_with_bad_email(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            user = UserMother.with_bad_email()

            await self.__creator(user.id.value, user.name.value, user.email.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()
