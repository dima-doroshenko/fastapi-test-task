from pydantic import BaseModel

class TaskCreateResponse(BaseModel):
    task_id: int

class TaskDeleteResponse(BaseModel):
    success: bool