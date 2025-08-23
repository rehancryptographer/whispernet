from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Voice-to-Everything")

class VoiceRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "voice-to-everything"}

@app.post("/voice")
def voice(req: VoiceRequest):
    # Dummy placeholder logic
    return {
        "status": "ok",
        "original": req.message,
        "converted": f"Voice version of [{req.message}]"
    }
