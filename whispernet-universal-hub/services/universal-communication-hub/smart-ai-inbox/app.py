from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Smart AI Inbox")

class Message(BaseModel):
    sender: str
    message: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "smart-ai-inbox"}

@app.get("/inbox/summary")
def inbox_summary():
    # Dummy placeholder logic
    sample_messages = [
        {"sender": "Alice", "message": "Meeting at 3PM"},
        {"sender": "Bob", "message": "Project update needed"}
    ]
    summary = f"{len(sample_messages)} messages today"
    return {"status": "ok", "summary": summary, "messages": sample_messages}
