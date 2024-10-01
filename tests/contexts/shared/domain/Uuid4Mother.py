from tests.contexts.shared.domain.MotherCreator import MotherCreator


class Uuid4Mother(MotherCreator):
    @classmethod
    def random(cls) -> str:
        return cls.get_faker().uuid4()
