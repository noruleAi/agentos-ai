from fastapi import FastAPI
import requests
import os
import uvicorn

app = FastAPI()

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
            "role": "user",
            "content": message
        }
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=payload
)

data = response.json()

return {
    "reply": data["choices"][0]["message"]["content"]
}