from collections import OrderedDict

from faker.providers import BaseProvider


class UserNameProvider(BaseProvider):
    def random_user_name(self) -> str:
        return self.random_element(OrderedDict([
            ('John Doe', 0.25), ('Margaret Jones', 0.25),
            ('Alfred Taylor', 0.25), ('Steve Conrad', 0.25),
        ]))

    def invalid_user_name(self) -> str:
        return self.random_element(OrderedDict([
            ('John.Doe', 0.25), ('@Margaret Jones', 0.25),
            ('Alfred_Taylor', 0.25), ('steve conrad', 0.25),
        ]))
