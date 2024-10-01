from typing import Any, Type
from abc import ABC, abstractmethod

from faker import Faker
from faker.providers import BaseProvider


class MotherCreator(ABC):
    __instance: Faker = None

    # @classmethod
    # @abstractmethod
    # def create(cls) -> Any:
    #     pass

    @classmethod
    @abstractmethod
    def random(cls) -> Any:
        pass

    # @classmethod
    # @abstractmethod
    # def invalid(cls) -> Any:
    #     pass

    @classmethod
    def get_faker(cls) -> Faker:
        if cls.__instance is None:
            cls.__instance = Faker()
        return cls.__instance

    @classmethod
    def add_provider(
            cls, provider: Type[BaseProvider]
    ) -> None:
        cls.get_faker().add_provider(provider)
