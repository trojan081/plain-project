from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import requests, os, traceback

router = APIRouter()

# URL Ollama из Docker-контейнера на Windows:
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434/api/chat")

# Загружаем базу знаний
with open("llm_base/project_info.md", encoding="utf-8") as f:
    KNOWLEDGE = f.read()

SYSTEM_PROMPT = (
    "Ты — эксперт по сервису plain-project.ru. Используй эту информацию:\n"
    + KNOWLEDGE +
    "\nОтвечай подробно и понятно."
)

@router.post("/llm_chat")
async def llm_chat(req: Request):
    try:
        data = await req.json()
        question = data.get("question", "")
        payload = {
            "model": "llama3",
            "stream": False,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": question}
            ]
        }
        resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
        resp.raise_for_status()
        j = resp.json()
        answer = j.get("message", {}).get("content", "⚠️ Модель вернула неожиданный ответ.")
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
    return {"answer": answer}
