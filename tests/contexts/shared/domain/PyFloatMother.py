from tests.contexts.shared.domain.MotherCreator import MotherCreator


class PyFloatMother(MotherCreator):
    @classmethod
    def random(
            cls, min_value: float = 1.0, max_value: float = 5_000.0, random_digits: int = 2,
    ) -> float:
        return cls.get_faker().pyfloat(min_value=min_value, max_value=max_value, right_digits=random_digits)
