from typing import List
from .base import BaseChunker, Chunk

class TextChunker(BaseChunker):
    def chunk(self, content: str) -> List[Chunk]:
        if not content.strip():
            return []

        return [
            Chunk(
                content=content.strip(),
                section_title=None,
                index=0,
            )
        ]
