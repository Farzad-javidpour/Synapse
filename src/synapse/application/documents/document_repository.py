from abc import ABC, abstractmethod

from synapse.application.documents.document_dtos import DocumentDto


class IDocumentRepository(ABC):

    @abstractmethod
    async def get_unprocessed_documents(
        self,
        limit: int = 100,
    ) -> list[DocumentDto]:
        ...