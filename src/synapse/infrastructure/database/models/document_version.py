from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from synapse.infrastructure.database.connection import Base

class DocumentVersion(Base):
    __tablename__ = "DocumentVersions"
    __table_args__ = {"schema": "DOC"}

    id: Mapped[int] = mapped_column(
        "Id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    document_id: Mapped[int] = mapped_column(
        "DocumentId",
        BigInteger,
        ForeignKey("DOC.Documents.Id"),
        nullable=False,
    )

    version_number: Mapped[int] = mapped_column(
        "VersionNumber",
        Integer,
        nullable=False,
    )

    file_name: Mapped[str] = mapped_column(
        "FileName",
        String(500),
        nullable=False,
    )

    file_extension: Mapped[str | None] = mapped_column(
        "FileExtension",
        String(20),
        nullable=True,
    )

    mime_type: Mapped[str | None] = mapped_column(
        "MimeType",
        String(100),
        nullable=True,
    )

    file_path: Mapped[str] = mapped_column(
        "FilePath",
        String(1000),
        nullable=False,
    )

    file_size_bytes: Mapped[int | None] = mapped_column(
        "FileSizeBytes",
        BigInteger,
        nullable=True,
    )

    file_hash: Mapped[str | None] = mapped_column(
        "FileHash",
        String(128),
        nullable=True,
    )

    page_count: Mapped[int] = mapped_column(
        "PageCount",
        Integer,
        nullable=False,
    )

    language_code: Mapped[str] = mapped_column(
        "LanguageCode",
        String(10),
        nullable=False,
    )

    processing_status_id: Mapped[int] = mapped_column(
        "ProcessingStatusId",
        Integer,
        nullable=False,
    )

    is_current: Mapped[bool] = mapped_column(
        "IsCurrent",
        Boolean,
        nullable=False,
    )

    error_message: Mapped[str | None] = mapped_column(
        "ErrorMessage",
        String(2000),
        nullable=True,
    )

    processed_at: Mapped[datetime | None] = mapped_column(
        "ProcessedAt",
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        "CreatedAt",
        DateTime,
        nullable=False,
    )

    created_by_personnel_code: Mapped[str | None] = mapped_column(
        "CreatedByPersonnelCode",
        String(50),
        nullable=True,
    )

    document = relationship(
        "Document",
        back_populates="versions",
    )