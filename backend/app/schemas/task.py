from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    prompt: str
    priority: Optional[str] = "normal"

class TaskResponse(BaseModel):
    task_id: str
    prompt: str
    result: str
    status: str
    created_at: Optional[datetime] = None