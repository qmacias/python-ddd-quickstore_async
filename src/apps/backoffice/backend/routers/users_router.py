import json

from typing import Dict, Any

from fastapi import APIRouter, Request, status
from fastapi.responses import Response, PlainTextResponse

from src.apps.container import container

from src.contexts.backoffice.users.application.BackofficeUserCreator import BackofficeUserCreator
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError

users_router = APIRouter()


@users_router.put('/users/{user_id}')
async def create_user(user_id: str, request: Request) -> Response:
    try:
        body: Dict[str, Any] = await request.json()

        await container.get(BackofficeUserCreator)(user_id, body.get('name'))

        return PlainTextResponse(None, status.HTTP_201_CREATED, {'Location': request.url.path})
    except InvalidArgumentError as e:
        return PlainTextResponse(json.dumps(str(e)), status.HTTP_422_UNPROCESSABLE_ENTITY, {'Location': request.url.path})
