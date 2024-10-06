from abc import ABC, abstractmethod


class EnvironmentArranger(ABC):
    @abstractmethod
    async def arrange(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
