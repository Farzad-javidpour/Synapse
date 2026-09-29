from abc import ABC, abstractmethod

from application.documents.models import Document


class DocumentRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Document]:
        raise NotImplementedError