from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import requests, os, traceback
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
    data = await req.json()
    question = data.get("question", "")
    prompt = format_alpaca_prompt(question)

    payload = {
        "model": "plain_model_4.0",
        "stream": True,
        "messages": [{"role": "user", "content": prompt}],
        "options": {
            "temperature": 0.2,
            "top_p": 0.8,
            "max_tokens": 4096,
            "do_sample": True,
            "stop": ["###", "### Инструкция:", "### Вводные данные:", "### Ответ:"]
        }
    }

    def generate_stream():
        with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as resp:
            for chunk in resp.iter_lines():
                if chunk:
                    try:
                        json_data = json.loads(chunk.decode('utf-8').strip())
                        if json_data.get("done"):
                            break
                        token = json_data.get("message", {}).get("content", "")
                        if token:
                            yield json.dumps({"token": token}) + "\n"
                    except json.JSONDecodeError:
                        continue
                    except Exception as e:
                        print(f"Error processing chunk: {e}")
                        traceback.print_exc()
                        break

    return StreamingResponse(generate_stream(), media_type="application/x-ndjson")
