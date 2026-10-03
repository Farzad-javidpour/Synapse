from fastapi import APIRouter, Depends, Request

from synapse.api.schemas.response import ApiResponse, success_response
from synapse.application.documents.document_dtos import DocumentDto
from synapse.application.documents.document_service import DocumentService
from synapse.composition.dependencies import get_document_service


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.get(
    "",
    response_model=ApiResponse[list[DocumentDto]],
)
async def get_documents(
    request: Request,
    service: DocumentService = Depends(get_document_service),
) -> ApiResponse[list[DocumentDto]]:

    documents = await service.get_documents_for_processing()

    return success_response(
        request=request,
        data=documents,
    )