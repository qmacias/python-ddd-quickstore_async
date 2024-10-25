from src.contexts.quickstore.products.domain.ProductId import ProductId


class ProductDoesNotExists(RuntimeError):
    def __init__(self, product_id: ProductId) -> None:
        super().__init__(f'Product {product_id.value!r} does not exists')
