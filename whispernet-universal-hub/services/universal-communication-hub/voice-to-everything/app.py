
from fastapi import FastAPI
app = FastAPI(title="Voice-to-Everything")

@app.post("/voice")
async def voice_to_text(payload: dict):
    return {"transcription": "This is a demo transcription"}
