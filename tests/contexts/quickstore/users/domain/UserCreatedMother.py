from src.contexts.quickstore.users.domain.UserCreated import UserCreated


class UserCreatedMother:
    @staticmethod
    def create(
            aggregate_id: str, name: str, email: str,
    ) -> 'UserCreated':
        return UserCreated(aggregate_id, name, email)
