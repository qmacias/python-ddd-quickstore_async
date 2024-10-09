from typing import Dict, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from src.contexts.shared.infrastructure.persistence.MongoConfig import MongoConfig


class MongoClientFactory:
    __clients: Dict[str, AsyncIOMotorClient] = {}

    @classmethod
    async def create_client(cls, context_name: str, config: MongoConfig) -> AsyncIOMotorClient:
        client = cls.__get_client(context_name)

        if not client:
            client = await cls.__create_and_connect_client(config)

            cls.__register_client(client, context_name)

        return client

    @classmethod
    def __get_client(cls, context_name: str) -> Optional[AsyncIOMotorClient]:
        return cls.__clients.get(context_name)

    @classmethod
    async def __create_and_connect_client(cls, config: MongoConfig) -> AsyncIOMotorClient:
        client = AsyncIOMotorClient(config.uri)

        await client.server_info()

        return client

    @classmethod
    def __register_client(cls, client: AsyncIOMotorClient, context_name: str) -> None:
        cls.__clients[context_name] = client
