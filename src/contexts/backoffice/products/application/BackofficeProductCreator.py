from logging import Logger

from src.contexts.shared.domain.EventBus import EventBus

from src.contexts.backoffice.products.domain.BackofficeProduct import BackofficeProduct
from src.contexts.backoffice.products.domain.BackofficeProductRepository import BackofficeProductRepository


class BackofficeProductCreator:
    def __init__(self, backoffice_repository: BackofficeProductRepository, event_bus: EventBus, logger: Logger) -> None:
        self.__backoffice_repository = backoffice_repository
        self.__eventbus = event_bus
        self.__logger = logger

    async def __call__(self, id: str, name: str) -> None:
        product = BackofficeProduct.create(id, name)

        await self.__backoffice_repository.save(product)

        events = product.pull_domain_events()

        await self.__eventbus.publish(events)

        self.__logger.info(
            'Backoffice Product Created',
            extra={'events': [event.to_primitives() for event in events]}
        )
