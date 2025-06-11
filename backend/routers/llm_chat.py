from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import requests, os, traceback
from fastapi.responses import JSONResponse, StreamingResponse 
import json

router = APIRouter()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434/api/chat")

def format_alpaca_prompt(instruction: str, input_text: str = "", output_text: str = "") -> str:
    return f"""Ниже приведена инструкция, описывающая задачу, в сочетании с вводными данными, предоставляющие последующий контекст запроса. Напиши ответ, который будет правильно отвечать на запрос.

### Инструкция:
{instruction}

### Вводные данные:
{input_text}

### Ответ:
{output_text}"""

@router.post("/llm_chat")
async def llm_chat(req: Request):
    try:
        data = await req.json()
        question = data.get("question", "")
        prompt = format_alpaca_prompt(question)

        payload = {
            "model": "plain_model_1.2",
            "stream": True,  # Включаем стриминг
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "options": {
                "temperature": 0.2,
                "top_p": 0.8,
                "max_tokens": 64
            }
        }

        # Отправляем запрос к Ollama
        resp = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) # stream=True для requests!
        resp.raise_for_status()

        async def generate_stream():
            for chunk in resp.iter_content(chunk_size=None): # Читаем поток по строкам
                if chunk:
                    try:
                        # Каждая строка - это отдельный JSON объект
                        # strip() убирает лишние пробелы и символы новой строки
                        json_data = json.loads(chunk.decode('utf-8').strip())
                        # Ollama возвращает 'done' когда ответ закончен
                        if json_data.get("done"):
                            break
                        # Извлекаем контент токена
                        token = json_data.get("message", {}).get("content", "")
                        if token:
                            # Отправляем каждый токен как отдельный JSON-объект
                            yield json.dumps({"token": token}) + "\n"
                    except json.JSONDecodeError:
                        # Игнорируем неполные или некорректные JSON-объекты,
                        # если такое вдруг случится в середине потока
                        continue
                    except Exception as e:
                        print(f"Error processing chunk: {e}")
                        traceback.print_exc()
                        break # Прерываем стриминг при ошибке

        # Возвращаем StreamingResponse
        # media_type очень важен, чтобы клиент знал, как парсить ответ
        return StreamingResponse(generate_stream(), media_type="application/x-ndjson")

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e), "trace": traceback.format_exc()})

