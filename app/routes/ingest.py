from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.ingestion.ingestion_service import IngestionService
from app.dependencies import get_ingestion_service

router = APIRouter()

class IngestRequest(BaseModel):
    path: str

@router.post("/ingest")
async def ingest(
    request: IngestRequest,
    service: IngestionService = Depends(get_ingestion_service)
):
    print('ingesting...')
    await service.process(request.path)
    print('ingested')
    return {"status": "processing_started"}
