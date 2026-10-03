from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DocumentVersionDto:
    id: int
    document_id: int
    version_number: int

    file_name: str
    file_extension: str | None
    mime_type: str | None
    file_path: str

    file_size_bytes: int | None
    file_hash: str | None

    page_count: int
    language_code: str

    processing_status_id: int
    is_current: bool

    error_message: str | None
    processed_at: datetime | None

    created_at: datetime
    created_by_personnel_code: str | None


@dataclass(frozen=True)
class DocumentDto:
    id: int
    code: str
    title: str
    description: str | None

    document_type_id: int
    document_category_id: int
    document_security_id: int
    document_status_id: int

    created_at: datetime
    updated_at: datetime | None

    current_version: DocumentVersionDto