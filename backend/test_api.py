from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()

@app.get("/")
async def root():
    return {
        "status": "AgentOS AI Running"
    }

@app.get("/debug")
async def debug():
    return {
        "has_key": bool(API_KEY),
        "length": len(API_KEY),
        "prefix": API_KEY[:8] if API_KEY else ""
    }

@app.get("/chat")
async def chat(message: str):

    if not API_KEY:
        return {
            "error": "OPENROUTER_API_KEY not found"
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://agentos-ai-production.up.railway.app",
        "X-Title": "AgentOS AI"
    }

    payload = {
        "model": "openai/gpt-4.1-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are AgentOS AI, an AI assistant created by Rahul Kumar Mahto. Always introduce yourself as AgentOS AI. Never introduce yourself as ChatGPT unless asked about the underlying AI model."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        if "choices" in data:
            return {
                "reply": data["choices"][0]["message"]["content"]
            }

        return {
            "error": data
        }

    except Exception as e:
        return {
            "error": str(e)
        }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )