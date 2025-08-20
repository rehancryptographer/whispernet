import os
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="WhisperNet API Gateway")

# Service registry
SERVICES = {
    "messaging": os.getenv("CPM_URL", "http://localhost:8010"),
    "ai_inbox": os.getenv("AI_INBOX_URL", "http://localhost:8011"),
    "one_click": os.getenv("ONE_CLICK_URL", "http://localhost:8012"),
    "voice": os.getenv("VOICE_URL", "http://localhost:8013"),
    "translate": os.getenv("TRANSLATE_URL", "http://localhost:8014"),
}

@app.get("/health")
async def health():
    return {"status": "ok", "service": "api-gateway"}


# ---------------- Messaging ----------------
@app.get("/messages/inbox")
async def inbox():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{SERVICES['messaging']}/messages/inbox", timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Messaging service failed: {str(e)}"})

@app.post("/messages/send")
async def send_message(request: Request):
    try:
        payload = await request.json()
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{SERVICES['messaging']}/messages/send", json=payload, timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Messaging service failed: {str(e)}"})


# ---------------- Smart AI Inbox ----------------
@app.get("/inbox/summary")
async def ai_summary():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{SERVICES['ai_inbox']}/inbox/summary", timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"AI Inbox failed: {str(e)}"})


# ---------------- One-Click Reply ----------------
@app.post("/reply")
async def one_click_reply(request: Request):
    try:
        payload = await request.json()
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{SERVICES['one_click']}/reply", json=payload, timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"One-Click Reply failed: {str(e)}"})


# ---------------- Voice-to-Everything ----------------
@app.post("/voice")
async def voice(request: Request):
    try:
        payload = await request.json()
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{SERVICES['voice']}/voice", json=payload, timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Voice service failed: {str(e)}"})


# ---------------- Multilingual Auto-Translate ----------------
@app.post("/translate")
async def translate(request: Request):
    try:
        payload = await request.json()
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{SERVICES['translate']}/translate", json=payload, timeout=10)
            return JSONResponse(status_code=r.status_code, content=r.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Translate service failed: {str(e)}"})
