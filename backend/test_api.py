from fastapi import FastAPI
import requests
import os

app = FastAPI()

# Read API key from Railway Variables
API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.get("/")
async def root():

    return {
        "status": "AgentOS AI Running"
    }

@app.get("/chat")
async def chat(message: str):

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
        }
    )

    data = response.json()

    print(data)

    if "choices" in data:

        reply = data["choices"][0]["message"]["content"]

    else:

        reply = str(data)

    return {
        "reply": reply
    }