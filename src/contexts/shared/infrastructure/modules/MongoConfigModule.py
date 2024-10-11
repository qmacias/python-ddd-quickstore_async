from injector import Module, singleton, provider

from settings import settings

from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig


class MongoConfigModule(Module):
    @singleton
    @provider
    def config_mongo(self) -> MongoConfig:
        mongoconfig = MongoConfig(uri=settings.MONGODB_URI)

        return mongoconfig


mongoconfig = MongoConfigModule()
