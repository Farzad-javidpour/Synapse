from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from synapse.infrastructure.database.connection import Base


class Document(Base):
    __tablename__ = "Documents"
    __table_args__ = {"schema": "DOC"}

    id: Mapped[int] = mapped_column(
        "Id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    code: Mapped[str] = mapped_column(
        "Code",
        String(50),
        nullable=False,
        unique=True,
    )

    title: Mapped[str] = mapped_column(
        "Title",
        String(400),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        "Description",
        String(2000),
        nullable=True,
    )

    document_type_id: Mapped[int] = mapped_column(
        "DocumentTypeId",
        Integer,
        nullable=False,
    )

    document_category_id: Mapped[int] = mapped_column(
        "DocumentCategoryId",
        Integer,
        nullable=False,
    )

    document_security_id: Mapped[int] = mapped_column(
        "DocumentSecurityId",
        Integer,
        nullable=False,
    )

    document_status_id: Mapped[int] = mapped_column(
        "DocumentStatusId",
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        "CreatedAt",
        DateTime,
        nullable=False,
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        "UpdatedAt",
        DateTime,
        nullable=True,
    )

    versions = relationship(
        "DocumentVersion",
        back_populates="document",
    )