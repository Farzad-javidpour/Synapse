from datetime import datetime
from pickletools import long4

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DocumentDbModel(Base):
    __tablename__ = "Documents"
    __table_args__ = {
        "schema": "DOC"
    }

    id: Mapped[int] = mapped_column(
        "Id",
        BigInteger,
        primary_key=True,
    )

    code: Mapped[str] = mapped_column(
        "Code",
        String(50),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        "Title",
        String(400),
        nullable=False,
    )