from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="One-Click Reply")

class ReplyRequest(BaseModel):
    message: str
    tone: str  # e.g., formal, casual

@app.get("/health")
def health():
    return {"status": "ok", "service": "one-click-reply"}

@app.post("/reply")
def one_click_reply(req: ReplyRequest):
    # Dummy placeholder logic
    return {
        "status": "ok",
        "original": req.message,
        "tone": req.tone,
        "reply": f"Auto-reply ({req.tone}) to: {req.message}"
    }
