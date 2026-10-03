from synapse.application.documents.document_dtos import DocumentDto
from synapse.application.documents.document_repository import IDocumentRepository


class DocumentService:

    def __init__(
        self,
        repository: IDocumentRepository,
    ):
        self._repository = repository

    async def get_documents_for_processing(
        self,
        limit: int = 100,
    ) -> list[DocumentDto]:

        return await self._repository.get_unprocessed_documents(
            limit=limit,
        )