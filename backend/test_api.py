from fastapi import FastAPI

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