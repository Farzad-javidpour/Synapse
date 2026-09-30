from synapse.domain.documents.entities import Document
from synapse.application.documents.repository import DocumentRepository


class DocumentService:

    def __init__(
        self,
        repository: DocumentRepository,
    ):
        self._repository = repository

    def get_all(self) -> list[Document]:
        return self._repository.get_all()

    def get_by_id(self, document_id: int) -> Document | None:
        return self._repository.get_by_id(document_id)