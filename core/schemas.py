from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    type: str
    description: str

class Plan(BaseModel):
    goal: str
    tasks: List[Task]

class ExecutionResult(BaseModel):
    task_id: int
    output: str
    confidence: float
