from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from synapse.api.schemas.response import ApiResponse, success_response
from synapse.application.documents.service import DocumentService
from synapse.composition.dependencies import get_document_service


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


class DocumentResponse(BaseModel):
    id: int
    code: str
    title: str


@router.get(
    "",
    response_model=ApiResponse[list[DocumentResponse]],
)
def get_documents(
    request: Request,
    service: DocumentService = Depends(get_document_service),
) -> ApiResponse[list[DocumentResponse]]:

    documents = service.get_all()

    response = [
        DocumentResponse(
            id=document.id,
            code=document.code,
            title=document.title,
        )
        for document in documents
    ]

    return success_response(
        request=request,
        data=response,
    )