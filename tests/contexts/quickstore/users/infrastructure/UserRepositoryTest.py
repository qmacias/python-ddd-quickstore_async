from typing import Callable, Awaitable
from unittest import IsolatedAsyncioTestCase

from src.apps.container import container

from src.contexts.quickstore.users.domain.UserRepository import UserRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.shared.domain.users.UserEmailProvider import UserEmailProvider
from tests.contexts.quickstore.users.domain.UserMother import UserMother


class UserRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        arranger_provider = container.get(
            Callable[[], Awaitable[EnvironmentArranger]],
        )

        self.__arranger = await arranger_provider()

        await self.__arranger.arrange()

    async def test_should_save_a_user(self) -> None:
        MotherCreator.add_provider(UserNameProvider)
        MotherCreator.add_provider(UserEmailProvider)

        user = UserMother.random()

        repository_provider = container.get(
            Callable[[], Awaitable[UserRepository]],
        )

        repository = await repository_provider()

        await repository.save(user)

    async def asyncTearDown(self):
        await self.__arranger.arrange()

        self.__arranger.close()
