# chunking/factory.py

from .code_chunker import CodeChunker
from .markdown_chunker import MarkdownChunker
from .text_chunker import TextChunker

def get_chunker(extension: str):
    if extension in [".py", ".ts", ".cs"]:
        return CodeChunker()
    elif extension == ".md":
        return MarkdownChunker()
    elif extension in [".txt", ".log", ".json", ".yaml", ".yml"]:
        return TextChunker()
    else:
        raise ValueError(f"Unsupported file extension: {extension}")
