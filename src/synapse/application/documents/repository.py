from abc import ABC, abstractmethod

from synapse.domain.documents.entities import Document


class DocumentRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Document]:
        pass

    @abstractmethod
    def get_by_id(self, document_id: int) -> Document | None:
        pass