from collections import OrderedDict

from faker.providers import BaseProvider


class UserEmailProvider(BaseProvider):
    def random_user_email(self) -> str:
        return self.random_element(OrderedDict([
            ('user@domain.com', 0.25), ('user123+tag@subdomain.domain.org', 0.25),
            ('name.surname@company.co.uk', 0.25), ('main-user@composite-domain.info', 0.25),
        ]))

    def invalid_user_email(self) -> str:
        return self.random_element(OrderedDict([
            ('user@domain', 0.25), ('user@.com', 0.25),
            ('@domain.com', 0.25), ('user@domain*com', 0.25),
        ]))
