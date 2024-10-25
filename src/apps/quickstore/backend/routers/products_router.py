import json

from typing import Annotated, Dict, Any, Callable, Awaitable

from fastapi import APIRouter, Body, Request, status
from fastapi.responses import Response, PlainTextResponse

from src.apps.container import container

from src.contexts.quickstore.productreviews.application.ProductReviewCreator import ProductReviewCreator
from src.contexts.shared.domain.InvalidArgumentError import InvalidArgumentError

products_router = APIRouter()


@products_router.put('/productreviews/{productreview_id}')
async def create_productreview(
        productreview_id: str, body: Annotated[Dict[str, Any], Body()], request: Request,
) -> Response:
    try:
        creator_provider = container.get(
            Callable[[], Awaitable[ProductReviewCreator]],
        )

        creator = await creator_provider()

        await creator(productreview_id, body.get('userId'), body.get('productId'), body.get('rating'))

        return PlainTextResponse(None, status.HTTP_201_CREATED, {'Location': request.url.path})
    except InvalidArgumentError as e:
        return PlainTextResponse(json.dumps(str(e)), status.HTTP_422_UNPROCESSABLE_ENTITY, {'Location': request.url.path})
