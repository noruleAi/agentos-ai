from fastapi import FastAPI
import requests
import os
import uvicorn

app = FastAPI()

# Read API key from Railway Variables
API_KEY = os.getenv("OPENROUTER_API_KEY")


@app.get("/")
async def root():
    return {
        "status": "AgentOS AI Running",
        "api_key_loaded": API_KEY is not None
    }


@app.get("/debug")
async def debug():
    return {
        "has_key": bool(API_KEY),
        "api_key_loaded": API_KEY is not None
    }


@app.get("/chat")
async def chat(message: str):

    if not API_KEY:
        return {
            "error": "OPENROUTER_API_KEY not found in Railway Variables"
        }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4.1-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "max_tokens": 200
            },
            timeout=30
        )

        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
            return {"reply": reply}

        return {"error": data}

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