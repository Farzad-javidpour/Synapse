from fastapi import APIRouter, Depends, Request

from synapse.api.schemas.response import ApiResponse, success_response
from synapse.application.llm.llm_dtos import ChatResponse
from synapse.application.llm.llm_service import LLMService
from synapse.composition.dependencies import get_llm_service

#===================================================
router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)
#===================================================
@router.get(
    "/chat",
    response_model=ApiResponse[ChatResponse],
)
async def chat(
    message: str,
    request: Request,
    service: LLMService = Depends(get_llm_service),
) -> ApiResponse[ChatResponse]:

    result = await service.chat(message=message)
    return success_response(
        request=request,
        data=result
    )
#===================================================