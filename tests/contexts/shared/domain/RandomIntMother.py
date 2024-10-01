from tests.contexts.shared.domain.MotherCreator import MotherCreator


class RandomIntMother(MotherCreator):
    @classmethod
    def random(cls, min: int = 1, max: int = 50) -> int:
        return cls.get_faker().random_int(min=min, max=max)
