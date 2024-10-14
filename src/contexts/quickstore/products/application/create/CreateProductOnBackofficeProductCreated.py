from injector import inject

from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.backoffice.products.domain.BackofficeProductCreated import BackofficeProductCreated


@inject
class CreateProductOnBackofficeProductCreated(EventSubscriber):
    __SUBSCRIPTIONS = [BackofficeProductCreated.EVENT_TYPE]

    def __init__(self, creator: ProductCreator) -> None:
        self.__creator = creator

    def subscribed_to(self) -> list[str]:
        return self.__SUBSCRIPTIONS

    async def on(self, event: BackofficeProductCreated) -> None:
        print(event.to_primitives())
        await self.__creator(event.aggregate_id, event.name)
