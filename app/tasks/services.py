from fastapi import HTTPException
from .models import Task

tasks_db = []

def find_task(task_id: int):
    for task in tasks_db:
        if task['id'] == task_id:
            return task
    return None

def create_task_service(task: Task):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="El título de la tarea no debe estar vacío")
    new_task = {"id": len(tasks_db) + 1, "title": task.title, "description": task.description}
    tasks_db.append(new_task)
    return new_task

def get_tasks_service():
    return tasks_db

def get_task_service(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

def update_task_service(task_id: int, updated_task: Task):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task['title'] = updated_task.title
    task['description'] = updated_task.description
    return task

def delete_task_service(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tasks_db.remove(task)
