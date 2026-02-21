from fastapi import APIRouter
from pydantic import BaseModel

ingest_router = APIRouter()
query_router = APIRouter()


class IngestRequest(BaseModel):
    source: str
    path: str


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5

@ingest_router.post("/ingest")
async def ingest(request: IngestRequest):
    # TODO: implement ingestion logic
    return {"status": "ingestion_started"}

@query_router.post("/query")
async def query(request: QueryRequest):
    # TODO: implement RAG logic
    return {
        "answer": "Stub response",
        "sources": [],
        "tokens_used": 0,
        "latency_ms": 0
    }