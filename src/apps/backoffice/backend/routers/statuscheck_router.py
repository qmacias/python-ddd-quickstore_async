from typing import Dict
from datetime import datetime

from fastapi import APIRouter, Request, status
from fastapi.responses import Response, PlainTextResponse

statuscheck_router = APIRouter()


@statuscheck_router.get("/")
async def root() -> Dict[str, str]:
    return {'app': 'Backoffice', 'time': str(datetime.now())}


@statuscheck_router.get("/status-check")
async def statuscheck(request: Request) -> Response:
    return PlainTextResponse(None, status.HTTP_200_OK, {'Location': request.url.path})
