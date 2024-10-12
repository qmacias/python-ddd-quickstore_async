from injector import Module, singleton, provider, multiprovider, inject
from typing import Awaitable, Callable

from src.contexts.shared.infrastructure.persistence.MongoClientFactory import MongoClientFactory
from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig
from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.quickstore.products.infrastructure.persistence.MongoProductRepository import MongoProductRepository
from src.contexts.quickstore.products.application.create.CreateProductOnBackofficeProductCreated import CreateProductOnBackofficeProductCreated
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository


class QuickstoreModule(Module):
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


class QuickstoreEventSubscribersModule(Module):
    @singleton
    @multiprovider
    @inject
    def event_subscribers(
            self,
            product_creator_provider: Callable[[], Awaitable[ProductCreator]],
    ) -> Callable[[], Awaitable[list[EventSubscriber]]]:
        async def __get_event_subscribers() -> list[EventSubscriber]:
            product_creator = await product_creator_provider()

            return [
                CreateProductOnBackofficeProductCreated(product_creator),
            ]

        return __get_event_subscribers
