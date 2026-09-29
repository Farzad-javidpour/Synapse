from fastapi import APIRouter, Request
from pydantic import BaseModel

from api.schemas.response import ApiResponse, success_response
from application.documents.service import DocumentService
from infrastructure.database.repositories.document_repository import (
    SqlServerDocumentRepository,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


class DocumentResponse(BaseModel):
    id: int
    code: str
    title: str


repository = SqlServerDocumentRepository()
service = DocumentService(repository)


@router.get(
    "",
    response_model=ApiResponse[list[DocumentResponse]],
)
def get_documents(
    request: Request,
) -> ApiResponse[list[DocumentResponse]]:

    documents = service.get_documents()

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