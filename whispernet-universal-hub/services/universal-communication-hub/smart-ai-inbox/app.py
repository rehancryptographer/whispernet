
from fastapi import FastAPI
app = FastAPI(title="Smart AI Inbox")

@app.get("/inbox/summary")
async def summary():
    return {"summary": "You have 3 important messages today", "messages": []}
