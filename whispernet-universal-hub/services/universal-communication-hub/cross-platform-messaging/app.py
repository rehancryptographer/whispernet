from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Multilingual Auto-Translate")

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "multilingual-auto-translate"}

@app.post("/translate")
def translate(req: TranslateRequest):
    return {
        "status": "ok",
        "original": req.text,
        "target_lang": req.target_lang,
        "translated": f"[{req.text}] in {req.target_lang}"
    }
