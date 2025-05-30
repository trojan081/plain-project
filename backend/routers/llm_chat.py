from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import requests, os, traceback

router = APIRouter()

# URL Ollama из Docker-контейнера на Windows:
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434/api/chat")

# Загружаем базу знаний
with open("llm_base/project_info.md", encoding="utf-8") as f:
    KNOWLEDGE = f.read()

# SYSTEM_PROMPT = (
#     "Ты — эксперт по сервису Plain. У тебя есть полная информация о функционале, типичных ошибках и способах их устранения.\n"
#     + KNOWLEDGE +
#     "\nВсегда отвечай только на русском языке. Если язык вопроса другой - используй в ответе язык, на котором пользователь задал вопрос. Пиши кратко, не более 100 слов. Не используй Markdown, не делай выделение жирным, не пиши заголовки, не добавляй эмодзи и спецсимволы. Пиши обычным текстом. Если пользователь запрашивает решение проблемы, либо глубокий вопрос, то ответы должны состоять из трёх частей:"
#     +
#     "1) Краткий вывод о том, что делать.\n"
#     +
#     "2) Пошаговая инструкция"  
#     + 
#     "3) Дополнительные советы или ссылки на документацию"
#     +
#     "Пиши не более 200 слов в дружелюбном и понятном стиле. Используй маркированные списки и подзаголовки."
#     +
#     "Если запрос неполный, попроси уточнить детали: ‘Можете уточнить, какой именно файл вы пытаетесь загрузить?’"
#     +
#     "Не придумывай новые функции сервиса и не упоминай возможности, которых нет в knowledge base. Если информации недостаточно — отвечай «Информация отсутствует» или проси уточнить вопрос."
# )

SYSTEM_PROMPT = (
    "Ты — эксперт по сервису Plain. "
    "Отвечай только на русском языке. Не используй английский ни в каких случаях. "
    "Отвечай только по теме сервиса, не придумывай новых функций. Не используй markdown и не выделяй текст. "
    "Пиши кратко и по делу, максимум 100 слов. Если ответа нет в knowledge base, скажи честно. "
    "\n\nПримеры вопросов и ответов:\n"
    "Вопрос: Как зарегистрироваться на сайте?\n"
    "Ответ: На главной странице нажмите «Регистрация», введите e-mail и пароль.\n"
    "Вопрос: Можно ли загрузить DWG-файл?\n"
    "Ответ: Пока только DXF. Поддержка DWG появится позже.\n"
    "\nВот информация о сервисе:\n" + KNOWLEDGE
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
