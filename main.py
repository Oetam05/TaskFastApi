from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Modelo de datos
class Task(BaseModel):
    title: str
    description: Optional[str] = ""

# Modelo de respuesta
class TaskResponse(Task):
    id: int

# Base de datos en memoria
tasks_db = []

def find_task(task_id: int):
    for task in tasks_db:
        if task['id'] == task_id:
            return task
    return None

# Endpoint para crear una nueva tarea
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="El título de la tarea no debe estar vacío")
    new_task = {"id": len(tasks_db) + 1, "title": task.title, "description": task.description}
    tasks_db.append(new_task)
    return new_task

# Endpoint para obtener todas las tareas
@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db

# Endpoint para obtener una tarea por su ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

# Endpoint para actualizar una tarea
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):
    if not updated_task.title.strip():
        raise HTTPException(status_code=400, detail="El título de la tarea no debe estar vacío")
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task['title'] = updated_task.title
    task['description'] = updated_task.description
    return task

# Endpoint para eliminar una tarea
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tasks_db.remove(task)
    return
