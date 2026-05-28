from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "sk-or-v1- d7bbb3126122552ede45dafcc8215a9995c90 fd2439c441e670e767156479e65""

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
