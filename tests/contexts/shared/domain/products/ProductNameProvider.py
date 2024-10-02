from collections import OrderedDict

from faker.providers import BaseProvider


class ProductNameProvider(BaseProvider):
    def random_product_name(self) -> str:
        return self.random_element(OrderedDict([
            ('Wireless Mouse', 0.25), ('Smartphone Case', 0.25),
            ('Bluetooth Speaker', 0.25), ('Gaming Monitor', 0.25),
        ]))

    def invalid_product_name(self) -> str:
        return self.random_element(OrderedDict([
            ('Wireless.Mouse', 0.25), ('@Smartphone Case', 0.25),
            ('Bluetooth_Speaker', 0.25), ('gaming monitor', 0.25),
        ]))
