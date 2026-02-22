from typing import List
from .base import BaseChunker, Chunk

class CodeChunker(BaseChunker):
    def chunk(self, content: str) -> List[Chunk]:
        return []
