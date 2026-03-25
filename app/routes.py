from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import Task, TaskCreate, TaskBase
from .manager import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=List[Task])
async def read_tasks():
    return task_service.get_all()

@router.post("", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    return task_service.create(task)

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskBase):
    result = task_service.update(task_id, task)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    if not task_service.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Successfully deleted"}