from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from synapse.application.documents.document_dtos import (
    DocumentDto,
    DocumentVersionDto,
)
from synapse.application.documents.document_repository import IDocumentRepository
from synapse.infrastructure.database.models.document import Document
from synapse.infrastructure.database.models.document_version import DocumentVersion


class SqlDocumentRepository(IDocumentRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_unprocessed_documents(
        self,
        limit: int = 100,
    ) -> list[DocumentDto]:

        statement = (
            select(Document, DocumentVersion)
            .join(
                DocumentVersion,
                DocumentVersion.document_id == Document.id,
            )
            .where(
                DocumentVersion.is_current == True,
                DocumentVersion.processing_status_id == 1,
            )
            #.order_by(Document.id)
            .limit(limit)
        )

        result = self._session.execute(statement)

        rows = result.all()

        return [
            self._to_dto(document, version)
            for document, version in rows
        ]

    @staticmethod
    def _to_dto(
        document: Document,
        version: DocumentVersion,
    ) -> DocumentDto:

        version_dto = DocumentVersionDto(
            id=version.id,
            document_id=version.document_id,
            version_number=version.version_number,

            file_name=version.file_name,
            file_extension=version.file_extension,
            mime_type=version.mime_type,
            file_path=version.file_path,

            file_size_bytes=version.file_size_bytes,
            file_hash=version.file_hash,

            page_count=version.page_count,
            language_code=version.language_code,

            processing_status_id=version.processing_status_id,
            is_current=version.is_current,

            error_message=version.error_message,
            processed_at=version.processed_at,

            created_at=version.created_at,
            created_by_personnel_code=version.created_by_personnel_code,
        )

        return DocumentDto(
            id=document.id,
            code=document.code,
            title=document.title,
            description=document.description,

            document_type_id=document.document_type_id,
            document_category_id=document.document_category_id,
            document_security_id=document.document_security_id,
            document_status_id=document.document_status_id,

            created_at=document.created_at,
            updated_at=document.updated_at,

            current_version=version_dto,
        )