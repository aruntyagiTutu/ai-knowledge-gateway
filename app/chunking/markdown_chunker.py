# app/chunking/markdown_chunker.py

import re
from typing import List
from app.chunking.base import BaseChunker, Chunk

class MarkdownChunker(BaseChunker):
    def __init__(
        self,
        max_chars: int = 1500,
        overlap: int = 200,
    ):
        self.max_chars = max_chars
        self.overlap = overlap

    def chunk(self, content: str) -> List[Chunk]:
        """
        Chunk markdown content by headings.
        Keeps heading + its section content together.
        Splits large sections further with overlap.
        """
        sections = self._split_by_headings(content)

        chunks: List[Chunk] = []
        chunk_index = 0

        for title, section_content in sections:
            if len(section_content) <= self.max_chars:
                chunks.append(
                    Chunk(
                        content=section_content.strip(),
                        section_title=title,
                        index=chunk_index,
                    )
                )
                chunk_index += 1
            else:
                # further split large section
                split_chunks = self._split_large_section(
                    section_content, title, chunk_index
                )
                chunks.extend(split_chunks)
                chunk_index += len(split_chunks)

        return chunks

    def _split_by_headings(self, content: str):
        """
        Splits markdown into sections based on headings.
        Returns list of (title, section_content).
        """

        pattern = r"(?m)^(#{1,6} .+)$"
        matches = list(re.finditer(pattern, content))

        if not matches:
            return [(None, content)]

        sections = []

        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)

            section_text = content[start:end]
            title = match.group(1)

            sections.append((title, section_text))

        return sections

    def _split_large_section(
        self, section: str, title: str | None, start_index: int
    ) -> List[Chunk]:
        """
        Split large section using sliding window with overlap.
        """

        chunks = []
        step = self.max_chars - self.overlap
        index = start_index

        for i in range(0, len(section), step):
            piece = section[i : i + self.max_chars]

            chunks.append(
                Chunk(
                    content=piece.strip(),
                    section_title=title,
                    index=index,
                )
            )
            index += 1

        return chunks
