
from fastapi import FastAPI
app = FastAPI(title="One-Click Reply")

@app.post("/reply")
async def reply(payload: dict):
    return {"original": payload.get("message"), "reply": "Thanks, got it!"}
