from pathlib import Path

from docx import Document


class WordDocumentLoader:

    def load(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Document file not found: {file_path}"
            )

        if path.suffix.lower() != ".docx":
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        document = Document(path)

        paragraphs = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)