from sqlalchemy.orm import Session, sessionmaker

from application.documents.models import Document
from application.documents.repository import DocumentRepository


class SqlServerDocumentRepository(DocumentRepository):

    def __init__(
        self,
        session_factory: sessionmaker[Session],
    ):
        self._session_factory = session_factory

    def get_all(self) -> list[Document]:
        with self._session_factory() as session:

            # فعلاً Mock
            return [
                Document(
                    id=1,
                    code="DOC-001",
                    title="Test Document",
                ),
                Document(
                    id=2,
                    code="DOC-002",
                    title="Second Document",
                ),
            ]