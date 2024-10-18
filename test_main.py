from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test para crear una tarea
def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task", "description": "Test description"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test description"
    assert data["id"] == 1

def test_create_task_empty_title():
    response = client.post("/tasks", json={"title": " ", "description": "Test description"})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "El título de la tarea no debe estar vacío"

# Test para obtener todas las tareas
def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Test Task"

# Test para obtener una tarea por ID
def test_get_task_by_id():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["id"] == 1

def test_get_task_by_invalid_id():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Tarea no encontrada"

# Test para actualizar una tarea
def test_update_task():
    response = client.put("/tasks/1", json={"title": "Updated Task", "description": "Updated description"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"

def test_update_task_empty_title():
    response = client.put("/tasks/1", json={"title": " ", "description": "Updated description"})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "El título de la tarea no debe estar vacío"

def test_update_task_invalid_id():
    response = client.put("/tasks/999", json={"title": "Updated Task", "description": "Updated description"})
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Tarea no encontrada"

# Test para eliminar una tarea
def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 204

def test_delete_task_invalid_id():
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Tarea no encontrada"