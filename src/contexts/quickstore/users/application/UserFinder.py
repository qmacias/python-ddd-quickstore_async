from src.contexts.quickstore.users.domain.User import User
from src.contexts.quickstore.users.domain.UserRepository import UserRepository
from src.contexts.quickstore.users.domain.UserFinder import UserFinder as DomainUserFinder


class UserFinder:
    def __init__(self, repository: UserRepository) -> None:
        self.__finder = DomainUserFinder(repository)

    async def __call__(self, id: str) -> User:
        return await self.__finder(id)
