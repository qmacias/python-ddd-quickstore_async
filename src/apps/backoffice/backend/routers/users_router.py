import json

from typing import Dict, Any, Callable, Awaitable

from fastapi import APIRouter, Request, status
from fastapi.responses import Response, PlainTextResponse

from src.apps.backoffice.backend.deps import backoffice_container

from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError

users_router = APIRouter()


@users_router.put('/users/{user_id}')
async def create_user(user_id: str, request: Request) -> Response:
    try:
        body: Dict[str, Any] = await request.json()

        creator_provider = backoffice_container.get(
            Callable[[], Awaitable[BackofficeUserCreator]],
        )

        creator = await creator_provider()

        await creator(user_id, body.get('name'))

        return PlainTextResponse(None, status.HTTP_201_CREATED, {'Location': request.url.path})
    except InvalidArgumentError as e:
        return PlainTextResponse(json.dumps(str(e)), status.HTTP_422_UNPROCESSABLE_ENTITY, {'Location': request.url.path})
