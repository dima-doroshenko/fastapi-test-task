from fastapi import APIRouter

from schemas import TaskCreate, TaskGet
from db import db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post('/')
async def create_task(task: TaskCreate) -> int:
    return db.add(task)

@router.get('/')
async def get_all_tasks() -> list[TaskGet]:
    return db.get_all()

@router.delete('/{id}')
async def delete_task(id: int) -> bool:
    return db.delete(id)