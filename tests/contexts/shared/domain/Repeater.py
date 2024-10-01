from tests.contexts.shared.domain.RandomIntMother import RandomIntMother


class Repeater:
    @staticmethod
    def random(function: callable, quantity: int = None) -> list:
        return [function() for _ in range(quantity or RandomIntMother.random(max=20))]
