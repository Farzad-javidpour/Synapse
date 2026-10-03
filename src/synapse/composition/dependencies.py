
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from synapse.application.documents.document_repository import IDocumentRepository
from synapse.application.documents.document_service import DocumentService
from synapse.infrastructure.database.repositories.document_repository import (
    SqlDocumentRepository,
)

from synapse.infrastructure.database.connection import get_db_session

from synapse.application.llm.llm_service import LLMService
from synapse.infrastructure.llm.client import LangChainLLMClient
from synapse.infrastructure.llm.factory import get_llm
from synapse.infrastructure.llm.providers import LLMProvider


def get_document_repository(
    session: AsyncSession = Depends(get_db_session),
) -> IDocumentRepository:

    return SqlDocumentRepository(session)


def get_document_service(
    repository: IDocumentRepository = Depends(get_document_repository),
) -> DocumentService:

    return DocumentService(repository)


def get_llm_service() -> LLMService:
    llm = get_llm(LLMProvider.OLLAMA)
    client = LangChainLLMClient(llm)
    return LLMService(client)