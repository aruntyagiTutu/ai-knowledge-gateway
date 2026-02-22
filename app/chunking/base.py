# app/chunking/base.py

from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass


@dataclass
class Chunk:
    content: str
    section_title: str | None
    index: int


class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, content: str) -> List[Chunk]:
        pass
