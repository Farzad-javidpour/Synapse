from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from synapse.application.documents.repository import DocumentRepository
from synapse.domain.documents.entities import Document
from synapse.infrastructure.database.models import DocumentDbModel


class SqlServerDocumentRepository(DocumentRepository):

    def __init__(
        self,
        session_factory: sessionmaker[Session],
    ):
        self._session_factory = session_factory

    def get_all(self) -> list[Document]:

        with self._session_factory() as session:

            statement = select(DocumentDbModel)

            rows = session.scalars(statement).all()

            return [
                Document(
                    id=row.id,
                    code=row.code,
                    title=row.title
                )
                for row in rows
            ]

    def get_by_id(
        self,
        document_id: int,
    ) -> Document | None:

        with self._session_factory() as session:

            statement = (
                select(DocumentDbModel)
                .where(DocumentDbModel.id == document_id)
            )

            row = session.scalar(statement)

            if row is None:
                return None

            return Document(
                    id=row.id,
                    code=row.code,
                    title=row.title
                )