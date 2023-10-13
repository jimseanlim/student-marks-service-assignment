from fastapi.routing import APIRouter

from app.api import (
    echo,
)

api_router = APIRouter()
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
