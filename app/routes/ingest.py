from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.ingestion_service import IngestionService
from app.dependencies import get_ingestion_service

router = APIRouter()

class IngestRequest(BaseModel):
    path: str

@router.post("/ingest")
async def ingest(
    request: IngestRequest,
    service: IngestionService = Depends(get_ingestion_service)
):
    service.process(request.path)
    return {"status": "processing_started"}
