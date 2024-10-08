from logging import Logger

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError
from src.contexts.shared.domain.EventBus import EventBus

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother
from tests.contexts.backoffice.users.domain.BackofficeUserCreatedMother import BackofficeUserCreatedMother


class BackofficeUserCreatorTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        MotherCreator.add_provider(UserNameProvider)

        self.__eventbus = AsyncMock(spec=EventBus)
        self.__repository = AsyncMock(spec=BackofficeUserRepository)

        self.__creator = (
            BackofficeUserCreator(self.__repository, self.__eventbus, AsyncMock(spec=Logger))
        )

    async def test_should_create_a_valid_backoffice_user(self) -> None:
        user = BackofficeUserMother.random()

        domain_events = [
            BackofficeUserCreatedMother
            .create(user.id.value, user.name.value)
        ]

        await self.__creator(user.id.value, user.name.value)

        self.__repository.save.assert_called_once_with(user)
        self.__eventbus.publish.assert_called_once_with(domain_events)

    async def test_should_not_create_an_invalid_backoffice_user_with_bad_id(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            user = BackofficeUserMother.with_bad_id()

            await self.__creator(user.id.value, user.name.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()

    async def test_should_not_create_an_invalid_backoffice_user_with_bad_name(self) -> None:
        with self.assertRaises(InvalidArgumentError):
            user = BackofficeUserMother.with_bad_name()

            await self.__creator(user.id.value, user.name.value)

            self.__repository.save.assert_not_called()
            self.__eventbus.publish.assert_not_called()
