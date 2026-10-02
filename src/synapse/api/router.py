from fastapi import APIRouter

from synapse.api.routes.health import router as health_router
from synapse.api.routes.document import router as document_router
from synapse.api.routes.llm import router as llm_router


api_router = APIRouter(
    prefix="/api/v1",
)

api_router.include_router(health_router)
api_router.include_router(llm_router)
api_router.include_router(document_router)