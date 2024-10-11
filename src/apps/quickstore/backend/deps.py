from injector import Module, singleton, provider, Injector
from typing import Awaitable, Callable

from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory
from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.infrastructure.modules.MongoConfigModule import mongoconfig
from src.contexts.shared.infrastructure.modules.EventBusModule import eventbus
from src.contexts.shared.infrastructure.modules.LoggerModule import logger

from src.contexts.quickstore.products.infrastructure.persistence.MongoProductRepository import MongoProductRepository
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.infrastructure.arranger.MongoEnvironmentArranger import MongoEnvironmentArranger


class QuickstoreModule(Module):
    @singleton
    @provider
    def environment_arranger(self, config: MongoConfig) -> Callable[[], Awaitable[EnvironmentArranger]]:
        async def __get_environment_arranger() -> EnvironmentArranger:
            client = await MongoClientFactory.create_client('quickstore', config)

            return MongoEnvironmentArranger(client, 'quickstore')

        return __get_environment_arranger

    @singleton
    @provider
    def product_repository(self, config: MongoConfig) -> Callable[[], Awaitable[ProductRepository]]:
        async def __get_product_repository() -> ProductRepository:
            client = await MongoClientFactory.create_client('products', config)

            return MongoProductRepository(client)

        return __get_product_repository

    @singleton
    @provider
    def product_creator(
            self,
            repository_provider: Callable[[], Awaitable[ProductRepository]],
    ) -> Callable[[], Awaitable[ProductCreator]]:
        async def __get_product_creator() -> ProductCreator:
            repository = await repository_provider()

            return ProductCreator(repository)

        return __get_product_creator


container = Injector(
    [mongoconfig, eventbus, logger, QuickstoreModule()], auto_bind=True,
)
