from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker

from synapse.application.documents.repository import DocumentRepository
from synapse.application.documents.service import DocumentService
from synapse.infrastructure.database.connection import SessionLocal
from synapse.infrastructure.database.repositories.document_repository import (
    SqlServerDocumentRepository,
)

from synapse.application.llm.llm_service import LLMService
from synapse.infrastructure.llm.client import LangChainLLMClient
from synapse.infrastructure.llm.factory import get_llm
from synapse.infrastructure.llm.providers import LLMProvider


def get_document_repository() -> DocumentRepository:
    return SqlServerDocumentRepository(session_factory=SessionLocal)


def get_document_service(repository: DocumentRepository = Depends(get_document_repository)) -> DocumentService:
    return DocumentService(repository)


def get_llm_service() -> LLMService:
    llm = get_llm(LLMProvider.OLLAMA)
    client = LangChainLLMClient(llm)
    return LLMService(client)