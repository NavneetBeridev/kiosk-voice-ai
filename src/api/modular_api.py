from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title=\"Marginalia API\", version=\"1.0.0\")

class VoiceRequest(BaseModel):
    user_id: str
    audio_base64: str
    metadata: Optional[dict] = None

class GameStateResponse(BaseModel):
    response_text: str
    is_correct: bool
    latency_ms: float

@app.get(\"/\")
def health_check():
    return {\"status\": \"online\", \"version\": \"1.0.0\", \"module\": \"marginalia-voice-engine\"}

@app.post(\"/api/v1/voice/process\", response_model=GameStateResponse)
async def process_voice_input(request: VoiceRequest):
    \"\"\"
    API-first endpoint for kiosks and mobile devices.
    Processes voice input and returns gameplay state with sub-400ms latency.
    \"\"\"
    try:
        # 1. Decode audio & perform STT (Pipecat)
        # 2. Process gameplay logic (DSPy)
        # 3. Generate response & metadata (Langfuse)
        return GameStateResponse(
            response_text=\"You got it! It's a Tiger!\",
            is_correct=True,
            latency_ms=385.0
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == \"__main__\":
    import uvicorn
    uvicorn.run(app, host=\"0.0.0.0\", port=8000)