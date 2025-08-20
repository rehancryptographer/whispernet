from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Cross-Platform Messaging Service")

# Temporary in-memory storage
MESSAGES = []

@app.get("/health")
async def health():
    return {"status": "ok", "service": "cross-platform-messaging"}

@app.get("/messages/inbox")
async def inbox():
    return {"messages": MESSAGES}

@app.post("/messages/send")
async def send_message(request: Request):
    payload = await request.json()
    message = {
        "from": payload.get("from"),
        "to": payload.get("to"),
        "message": payload.get("message"),
    }
    MESSAGES.append(message)
    return {"status": "sent", **message}
