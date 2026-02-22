# app/services/ingestion_service.py

from app.ingestion.file_validator import validate_file_path
from app.chunking.factory import get_chunker

class IngestionService:
    async def process(self, file_path: str):
        path = validate_file_path(file_path)
        print(path)
        content = path.read_text(encoding="utf-8")
        print('chunking...')
        chunker = get_chunker(path.suffix)
        chunks = chunker.chunk(content)
        print('chunks:', len(chunks))
