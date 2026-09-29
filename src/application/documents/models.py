from dataclasses import dataclass


@dataclass
class Document:
    id: int
    code: str
    title: str