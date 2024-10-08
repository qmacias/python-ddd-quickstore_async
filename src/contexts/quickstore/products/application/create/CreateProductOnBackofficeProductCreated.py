from injector import inject

from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.backoffice.products.domain.BackofficeProductCreated import BackofficeProductCreated

from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator


@inject
class CreateProductOnBackofficeProductCreated(EventSubscriber):
    __SUBSCRIPTIONS = [BackofficeProductCreated.EVENT_TYPE]

    def __init__(self, creator: ProductCreator) -> None:
        self.__creator = creator

    def subscribed_to(self) -> list[str]:
        return self.__SUBSCRIPTIONS

    async def on(self, event: BackofficeProductCreated) -> None:
        await self.__creator(event.aggregate_id, event.name)
