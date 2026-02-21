from fastapi import FastAPI
from app.routes import ingest_router, query_router

app = FastAPI(
    title="AI Knowledge Gateway",
    version="0.1.0",
    description="RAG-based internal knowledge API"
)


# Register routers
app.include_router(ingest_router, prefix="/api")
app.include_router(query_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}