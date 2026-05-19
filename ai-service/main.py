from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import predict

app = FastAPI(
    title="AgroShield AI Service",
    description="Crop disease detection and agricultural AI inference API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/api", tags=["predict"])


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "agroshield-ai-service"}
