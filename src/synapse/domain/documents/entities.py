from dataclasses import dataclass
from datetime import datetime


@dataclass
class Document:
    id: int
    code: str
    title: str