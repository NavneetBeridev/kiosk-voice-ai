from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional, Dict
import time
import logging

# API Orchestration for Kiosk AI Engine
app = FastAPI(title=\"Kiosk Voice API\", version=\"1.1.0\")
logger = logging.getLogger(\"KioskAPI\")

class TurnRequest(BaseModel):
    user_id: str
    audio_stream_id: str
    input_text: str
    target_id: str
    metadata: Optional[Dict] = None

class TurnResponse(BaseModel):
    response_text: str
    is_correct: bool
    latency_ms: float
    session_id: str

@app.middleware(\"http\")
async def log_latency(request: Request, call_next):
    \"\"\"Middleware for real-time latency monitoring across the engine.\"\"\"
    start_time = time.time()
    response = await call_next(request)
    latency = (time.time() - start_time) * 1000
    logger.info(f\"{request.url.path} latency: {latency:.2f}ms\")
    return response

@app.post(\"/api/v1/voice/turn\", response_model=TurnResponse)
async def handle_turn(request: TurnRequest):
    \"\"\"
    Processes a single voice turn for kiosks and mobile devices.
    Orchestrates Pipecat, DSPy, and Langfuse monitoring.
    \"\"\"
    try:
        # Mocking the engine orchestration loop
        return TurnResponse(
            response_text=\"Spot on! It's a Tiger!\",
            is_correct=True,
            latency_ms=385.4,
            session_id=request.audio_stream_id
        )
    except Exception as e:
        logger.error(f\"Turn processing failed: {e}\", exc_info=True)
        raise HTTPException(status_code=500, detail=\"Internal processing error\")

if __name__ == \"__main__\":
    import uvicorn
    uvicorn.run(app, host=\"0.0.0.0\", port=8000)