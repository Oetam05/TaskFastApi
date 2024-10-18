from fastapi import FastAPI
from app.tasks import routes as task_routes

app = FastAPI()

# Incluir las rutas de "tasks"
app.include_router(task_routes.router)
