from fastapi import APIRouter

from schemas import (
    TaskCreate,
    TaskGet,
    TaskCreateResponse,
    TaskDeleteResponse,
)
from db import db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("/")
async def create_task(task: TaskCreate) -> TaskCreateResponse:
    return TaskCreateResponse(
        task_id=db.add(task)
    )


@router.get("/")
async def get_all_tasks() -> list[TaskGet]:
    return db.get_all()


@router.delete("/{id}")
async def delete_task(id: int) -> TaskDeleteResponse:
    return TaskDeleteResponse(
        success=db.delete(id)
    )
