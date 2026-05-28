from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():

    return {
        "status": "AgentOS AI Running"
    }

@app.get("/chat")
async def chat(message: str):

    return {
        "reply": "Hello " + message
    }

uvicorn.run(app, host="0.0.0.0", port=8000)
