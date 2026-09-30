from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker

from synapse.application.documents.repository import DocumentRepository
from synapse.application.documents.service import DocumentService
from synapse.infrastructure.database.connection import SessionLocal
from synapse.infrastructure.database.repositories.document_repository import (
    SqlServerDocumentRepository,
)


def get_document_repository() -> DocumentRepository:
    return SqlServerDocumentRepository(
        session_factory=SessionLocal
    )


def get_document_service(
    repository: DocumentRepository = Depends(get_document_repository),
) -> DocumentService:

    return DocumentService(repository)