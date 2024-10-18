from fastapi import APIRouter, HTTPException
from .models import Task, TaskResponse
from .services import create_task_service, get_task_service, update_task_service, delete_task_service, get_tasks_service

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    return create_task_service(task)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return get_tasks_service()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    return get_task_service(task_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):
    return update_task_service(task_id, updated_task)

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    delete_task_service(task_id)
    return None
