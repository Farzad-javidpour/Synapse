from fastapi import APIRouter

from api.routes.health import router as health_router
from api.routes.document import router as document_router


api_router = APIRouter(
    prefix="/api/v1",
)

api_router.include_router(health_router)
api_router.include_router(document_router)