from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.backoffice.users.domain.BackofficeUserMother import BackofficeUserMother


class BackofficeUserRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_save_a_backoffice_user(self) -> None:
        MotherCreator.add_provider(UserNameProvider)

        user = BackofficeUserMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[BackofficeUserRepository]],
        )

        repository = await repository_provider()

        await repository.save(user)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
