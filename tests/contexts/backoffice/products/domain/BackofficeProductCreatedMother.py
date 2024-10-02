from src.contexts.backoffice.products.domain.BackofficeProductCreated import BackofficeProductCreated


class BackofficeProductCreatedMother:
    @staticmethod
    def create(
            aggregate_id: str, name: str,
    ) -> 'BackofficeProductCreated':
        return BackofficeProductCreated(aggregate_id, name)
