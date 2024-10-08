from injector import Module, singleton, provider, multiprovider, inject

from src.apps.quickstore.backend.settings import settings
from src.contexts.shared.domain.EventSubscriber import EventSubscriber

from src.contexts.quickstore.products.infrastructure.persistence.MongoProductRepository import MongoProductRepository
from src.contexts.quickstore.products.infrastructure.persistence.InMemoryProductRepository import InMemoryProductRepository
from src.contexts.quickstore.products.application.create.CreateProductOnBackofficeProductCreated import CreateProductOnBackofficeProductCreated
from src.contexts.quickstore.products.application.create.ProductCreator import ProductCreator
from src.contexts.quickstore.products.domain.ProductRepository import ProductRepository

from tests.contexts.shared.infrastructure.arranger.EnvironmentArranger import EnvironmentArranger
from tests.contexts.shared.infrastructure.arranger.mongo.MongoEnvironmentArranger import MongoEnvironmentArranger

QUICKSTORE_MONGODB_URI = settings.MONGODB_URI


class QuickstoreModule(Module):
    @singleton
    @provider
    def environment_arranger(self) -> EnvironmentArranger:
        return MongoEnvironmentArranger(QUICKSTORE_MONGODB_URI, 'quickstore')

    @singleton
    @provider
    def product_repository(self) -> ProductRepository:
        # repository = InMemoryProductRepository()
        repository = MongoProductRepository(QUICKSTORE_MONGODB_URI)

        return repository

    @singleton
    @provider
    def product_creator(
            self, repository: ProductRepository,
    ) -> ProductCreator:
        return ProductCreator(repository)

    @singleton
    @provider
    def create_product_on_backoffice_product_created_subscriber(
            self, creator: ProductCreator,
    ) -> EventSubscriber:
        return CreateProductOnBackofficeProductCreated(creator)


class QuickstoreEventSubscribersModule(Module):
    @singleton
    @multiprovider
    @inject
    def event_subscribers(
            self,
            creator: ProductCreator,
    ) -> list[EventSubscriber]:
        return [
            CreateProductOnBackofficeProductCreated(creator),
        ]
