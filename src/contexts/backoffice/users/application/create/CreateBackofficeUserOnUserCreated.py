from injector import inject

from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.backoffice.users.application.create.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.quickstore.users.domain.UserCreated import UserCreated


@inject
class CreateBackofficeUserOnUserCreated(EventSubscriber):
    __SUBSCRIPTIONS = [UserCreated.EVENT_TYPE]

    def __init__(self, creator: BackofficeUserCreator) -> None:
        self.__creator = creator

    def subscribed_to(self) -> list[str]:
        return self.__SUBSCRIPTIONS

    async def on(self, event: UserCreated) -> None:
        print(event.to_primitives())
        await self.__creator(event.aggregate_id, event.name, event.email)
