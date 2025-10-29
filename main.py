from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API with FastAPI")

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

tasks = [
    Task(id=1, title="Learn CI/CD"),
    Task(id=2, title="Build FastAPI project")
]

@app.get("/")
def home():
    return {"message": "FastAPI app deployed via CI/CD on Render!  ***** to test if it changes without manually deploy.."}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
def mark_done(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted"}

