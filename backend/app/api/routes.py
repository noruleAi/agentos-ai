from fastapi import APIRouter, Depends, HTTPException, status
from app.agents.planner_agent import planner_agent
from app.agents.coding_agent import coding_agent
from app.agents.research_agent import research_agent
from app.schemas.task import TaskCreate, TaskResponse
from app.core.auth import get_current_user
from app.core.database import get_db

router = APIRouter(prefix="/api", tags=["tasks"])

@router.post("/tasks/create", response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    current_user = Depends(get_current_user),
    db = Depends(get_db)
):
    """Create and execute an AI task"""
    try:
        if "code" in task.prompt.lower():
            result = await coding_agent(task.prompt)
        elif "research" in task.prompt.lower():
            result = await research_agent(task.prompt)
        else:
            result = await planner_agent(task.prompt)
        
        return TaskResponse(
            task_id="task_123",
            prompt=task.prompt,
            result=result,
            status="completed"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/tasks/{task_id}")
async def get_task(
    task_id: str,
    current_user = Depends(get_current_user)
):
    """Get task status and results"""
    return {
        "task_id": task_id,
        "status": "completed",
        "result": "Task result data"
    }

@router.get("/memory")
async def get_memory(current_user = Depends(get_current_user)):
    """Retrieve user memory"""
    return {
        "memories": []
    }

@router.post("/memory/save")
async def save_memory(
    data: dict,
    current_user = Depends(get_current_user)
):
    """Save to user memory"""
    return {"saved": True}