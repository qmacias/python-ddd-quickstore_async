from src.contexts.quickstore.users.domain.UserId import UserId


class UserDoesNotExists(RuntimeError):
    def __init__(self, user_id: UserId) -> None:
        super().__init__(f'User {user_id.value!r} does not exists')
