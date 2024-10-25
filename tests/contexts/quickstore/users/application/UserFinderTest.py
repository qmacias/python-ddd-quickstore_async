from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.contexts.quickstore.users.application.UserFinder import UserFinder
from src.contexts.quickstore.users.domain.UserRepository import UserRepository
from src.contexts.quickstore.users.domain.UserDoesNotExists import UserDoesNotExists

from tests.contexts.shared.domain.MotherCreator import MotherCreator
from tests.contexts.shared.domain.users.UserNameProvider import UserNameProvider
from tests.contexts.shared.domain.users.UserEmailProvider import UserEmailProvider
from tests.contexts.quickstore.users.domain.UserMother import UserMother


class UserFinderTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        MotherCreator.add_provider(UserNameProvider)
        MotherCreator.add_provider(UserEmailProvider)

        self.__repository = AsyncMock(spec=UserRepository)

        self.__finder = UserFinder(self.__repository)

    async def test_should_find_an_existing_user(self) -> None:
        existing_user = UserMother.random()

        self.__repository.search.return_value = existing_user

        expected_user = await self.__finder(existing_user.id.value)

        self.__repository.search.assert_called_once_with(existing_user.id)
        self.assertEqual(existing_user, expected_user)

    async def test_should_raise_an_exception_when_user_does_not_exists(self) -> None:
        user = UserMother.random()

        self.__repository.search.return_value = None

        with self.assertRaises(UserDoesNotExists):
            await self.__finder(user.id.value)

            self.__repository.search.assert_called_once_with(user.id)
