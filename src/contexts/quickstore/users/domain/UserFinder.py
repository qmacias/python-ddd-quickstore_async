from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserId import UserId
from src.contexts.quickstore.users.domain.UserRepository import UserRepository
from src.contexts.quickstore.users.domain.UserDoesNotExists import UserDoesNotExists


class UserFinder:
    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    async def __call__(self, id: str) -> User:
        user_id = UserId(id)

        user = await self.__repository.search(user_id)

        if not user:
            raise UserDoesNotExists(user_id)

        return user
