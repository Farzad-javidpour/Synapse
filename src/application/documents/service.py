from .models import Document
from .repository import DocumentRepository


class DocumentService:

    def __init__(
        self,
        repository: DocumentRepository,
    ):
        self.repository = repository

    def get_documents(self) -> list[Document]:
        return self.repository.get_all()