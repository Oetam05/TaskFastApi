from pydantic import BaseModel
from typing import Optional

# Modelo para los datos de entrada
class Task(BaseModel):
    title: str
    description: Optional[str] = ""

# Modelo para las respuestas de la API
class TaskResponse(Task):
    id: int
