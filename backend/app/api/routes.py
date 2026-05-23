from fastapi import APIRouter
from app.agents.planner_agent import planner_agent
from app.memory.memory_manager import save_memory
from app.memory.memory_manager import get_memories

router = APIRouter()

@router.post("/task/create")
async def create_task(prompt: str):

    result = await planner_agent(prompt)

    await save_memory({
        "prompt": prompt,
        "result": result
    })

    return {
        "task": prompt,
        "result": result,
        "status": "completed"
    }

@router.get("/memory")
async def memory():

    memories = await get_memories()

    return {
        "memories": memories
    }