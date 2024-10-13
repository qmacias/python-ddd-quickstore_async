from src.contexts.backoffice.users.domain.BackofficeUserCreated import BackofficeUserCreated


class BackofficeUserCreatedMother:
    @staticmethod
    def create(
            aggregate_id: str, name: str, email: str,
    ) -> 'BackofficeUserCreated':
        return BackofficeUserCreated(aggregate_id, name, email)
