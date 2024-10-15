import json

from typing import Annotated, Dict, Any, Callable, Awaitable

from fastapi import APIRouter, Body, Request, status
from fastapi.responses import Response, PlainTextResponse

from src.apps.container import container

from src.contexts.quickstore.users.application.UserCreator import UserCreator
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError

users_router = APIRouter()


@users_router.put('/users/{user_id}')
async def create_user(
        user_id: str, body: Annotated[Dict[str, Any], Body()], request: Request,
) -> Response:
    try:
        creator_provider = container.get(
            Callable[[], Awaitable[UserCreator]],
        )

        creator = await creator_provider()

        await creator(user_id, body.get('name'), body.get('email'))

        return PlainTextResponse(None, status.HTTP_201_CREATED, {'Location': request.url.path})
    except InvalidArgumentError as e:
        return PlainTextResponse(json.dumps(str(e)), status.HTTP_422_UNPROCESSABLE_ENTITY, {'Location': request.url.path})
